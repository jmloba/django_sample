from django.shortcuts import render,HttpResponse
from app_invoice.models import Invoice

from django.db.models import Sum, Q
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch,cm
from reportlab.lib.pagesizes import A4
from reportlab.lib import utils
from reportlab.platypus import Frame, Image
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer,  Preformatted, XPreformatted 
from reportlab.platypus.tables import Table, TableStyle, colors
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch

from .invtemplate import print_template,reference_code_print



# Create your views here.


def print_invoice_now(invoice_list,pdf_path,invoice_no):
  mypath = pdf_path
  
  
  rowcount =1
  global mtotals 
  mtotals= 0.0
  y_axis = 6.0
  global  page_total 
  page_total = 0.0
  g_total = 0.0
  pageno =1
  
  c=canvas.Canvas(mypath, pagesize=A4)
  c.translate(inch, inch)  # x y position using inch  

  c,pageno = print_template(c,pageno,invoice_no)  


  for row_number, row_data in enumerate(invoice_list):
    # print_letter_heading(c)
    rowcount += 1
    page_total = print_body_data(c, row_data ,y_axis, page_total)
    y_axis -= 0.3

    if rowcount > 3 :
        print_pagetotal(c,page_total)
        g_total += page_total
        page_total = 0.0
        c.showPage()
        c.translate(inch, inch)
        c,pageno = print_template(c,pageno,invoice_no)  # load template
 
        y_axis = 6.0
        rowcount = 1
  g_total += page_total
  print_pagetotal(c,page_total)
  print_page_grand_total(c,g_total)
  c.showPage()
  c.save()

def print_pagetotal(c,page_total):
    c.setFillColor('#071952')
    c.setFont("Helvetica", 15)
    c.drawString(-.5*inch,2*inch, "Page Total :")

    c.setFillColor('#884A39')
    c.drawString(2*inch,2*inch, str(page_total))

def print_page_grand_total(c, g_total):
    c.setFillColor('#071952')
    c.setFont("Helvetica", 15)
    c.drawString(-.5*inch,1.7*inch, "Grand Total :")



    c.setFillColor('#fd1f1f')
    c.drawString(2*inch,1.7*inch, str(g_total))


def print_body_data(c,row_data, y_axis,page_total):

    
  c.setFillColorCMYK(1,0,0,89)

  c.setFont("Helvetica", 14)

  print(f'\n\n row data : \n {row_data}')

  mdesc = row_data['description']
  mqty =  str(row_data['quantity'])
  mamt = str(row_data['amount'])

  page_total += float(row_data['amount'])
  # mtotals +=row_data['amount']

  c.drawString(-.5*inch, y_axis * inch, mdesc)
  c.drawString(1*inch, y_axis * inch, mqty)
  c.drawString(4*inch, y_axis * inch, mamt)
  return page_total

def get_invoice_to_print(new_invoice):
  mdata = Invoice.objects.filter(invoice_no = new_invoice).values('invoice_no', 'description', 'quantity','price','amount')
  invoice_list= list(mdata)   

  return invoice_list

def print_invoice(request,new_invoice):
  invoice_list = get_invoice_to_print(new_invoice)

  if invoice_list==None:
    return HttpResponse('Nothing to print ... app_print/print_invoice')

  
  if  invoice_list:
    mypath = 'c:/reportlab/invoice.pdf'
    print_invoice_now(invoice_list,mypath,new_invoice)
  else  :
    mypath=''
    print('nothing to print')
  context={'invoice_list':invoice_list ,'mypath':mypath  }
  return render(request,'app_print/print-invoice.html' ,context ) 

def reprint_invoice(request):
  context={  }
  return render(request,'app_print/reprint-invoice.html' ,context ) 



def add_all_values (qs,simple_list):
  # add all values
  myValues = list(qs.values_list())


  print(f'myValues :\n{myValues} \n\n')
  for i in myValues:
    simple_list.append(i)

  return simple_list
 
def get_tableheader(qs):
  header = qs[0].__dict__.keys()
  mheader =[]

  for  i in header:
    print(f'counter : {i}')
    if i!='_state':
      mheader.append(i)
  return mheader  

def  create_simple_table(invno):
  

  print(f'\nsum quantity : using aggregate')
  qs= Invoice.objects.filter(invoice_no=invno)
  #qs getting the total amount
  qs_sum = Invoice.objects.filter(invoice_no=invno).aggregate(Sum('quantity'))
  simple_list=[]
  simple_list.append(get_tableheader(qs))
  simple_list = add_all_values(qs,simple_list)
  print(f'\n\nsimple list : \n{simple_list}') 
  


def print_invoice_tabular(request):
  mypath='c:/reportlab/tabular.pdf'
  print('recordset')
  qs=Invoice.objects.filter(invoice_no =4) 
  simple_list=[]
  simple_list.append(get_tableheader(qs))
  mydata = add_all_values(qs,simple_list)
  print('------')
  print(f'simple list : \n\n {simple_list} ')

  mydoc = SimpleDocTemplate(mypath, pagesize=letter)
  
  # t=Table(mydata, rowHeights=80, repeatRows=1)
  '''setting the column width '''
  c_width=[0.5*inch,   0.5*inch, 0.75*inch,   
           .9*inch,   2.0*inch, 0.7*inch,   
           1.5*inch, 0.5*inch,   
           ]
  t=Table(mydata, rowHeights=80, repeatRows=1,colWidths=c_width)

  '''setting table style'''
  t.setStyle(TableStyle([
    ('BACKGROUND',(0,0),(-1,0),colors.lightgreen),
    
    # '''line 2 color yellow'''
    ('BACKGROUND',(0,2),(-1,0),colors.yellow),

    # '''line 2 color blue'''
    ('BACKGROUND',(2,3),(2,4),colors.green),

    ('FONTSIZE',(0,0),(-1,-1),8)
    ],
  ))


  elements=[]
  elements.append(t)
  mydoc.build(elements)



  context={}
  return render(request,'app_print/print-invoice-tabular.html' ,context ) 
 
