from django.shortcuts import render
from app_invoice.models import Invoice

from reportlab.pdfgen import canvas
from reportlab.lib.units import inch,cm
from reportlab.lib.pagesizes import A4, letter
from reportlab.lib import utils
from reportlab.platypus import Frame, Image
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Preformatted, XPreformatted
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch

from .invtemplate import my_temp,reference_code_print


# Create your views here.





def print_invoice_now(invoice_list):
  mypath = 'c:/reportlab/invoice.pdf'
  c=canvas.Canvas(mypath, pagesize=A4)
  c.translate(inch, inch)  # x y position using inch
  rowcount =1
  global mtotals 
  mtotals= 0.0
  #load a template
  
  reference_code_print(c)  

  y_axis = 6.0
  global  page_total 
  page_total = 0.0
  g_total = 0.0
  pageno =1
  c,pageno = my_temp(c,pageno)  


  for row_number, row_data in enumerate(invoice_list):
    # print_letter_heading(c)
    rowcount += 1
    page_total = print_body_data(c, row_data ,y_axis, page_total)
    y_axis -= 0.3

    if rowcount > 8 :
        print_pagetotal(c,page_total)
        g_total += page_total
        page_total = 0.0
        c.showPage()
        c,pageno = my_temp(c,pageno)  # load template
        reference_code_print(c)
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

def print_invoice(request):
  mdata = Invoice.objects.filter(invoice_no = 4).values('invoice_no', 'description', 'quantity','price','amount')

  invoice_list= list(mdata)  


  print(f'\n\ninvoice_db: {mdata}')
  print(f'\n\n (list) invoice_db: {invoice_list} \n')

  if  invoice_list:
    print_invoice_now(invoice_list)
  else  :
    print('nothing to print')

  context={'invoice_list':invoice_list   }
  return render(request,'app_print/print-invoice.html' ,context ) 
 
