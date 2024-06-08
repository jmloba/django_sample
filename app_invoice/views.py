from django.http import JsonResponse, FileResponse,HttpResponse
from django.db.models import Sum, Q
from django.shortcuts import redirect, render
from .forms import InvoiceForm, InvoiceSearchForm, Date_Sample1

from .models import Invoice,Customer, Ref_Table, InvoiceSummary
from app_accounts.utils import reformat_date
import io
from app_print.views import print_invoice

# printing
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

from reportlab.lib.pagesizes import A4, letter






# Create your views here.
def invoice_create(request):
  title ="Invoice Section"
  card_title='Invoice Entry'

  invoice_form =InvoiceForm()
  search_form = InvoiceSearchForm()
  mdata = Invoice.objects.filter(user=request.user, invoice_no = 0 ).values('id','customer','customer__name','description','invoice_date','quantity','price','amount')
  invoice_db= list(mdata)  
  for i in invoice_db:
    i['invoice_date'] = reformat_date(i['invoice_date'] )
  print(f'invoice_db-->> : {invoice_db}')
  
  if request.method=='POST':
    print('request is post....')
    search_form = InvoiceSearchForm(request.POST or None)
    invoice_db=Invoice.objects.filter(user=request.user ,description__icontains=search_form['description'].value( ))     
  else:
    print('request is GET')


  context={'title':title,
           "card_title": card_title,
           "invoice_form": invoice_form, 
           "search_form":search_form,
           "invoice_db":invoice_db          
           }
  
  
  return render(request,'app_invoice/create_invoice.html', context)


def search_desc(request):
  print ('views search')
  
def reformat_date(datestr):
  new_format='jov'
  return new_format


def data_list(request,invno)  :
  invoicedata =   Invoice.objects.filter(user=request.user, invoice_no = invno).values('id','customer','customer__name','invoice_no','description','invoice_date','quantity', 'price', 'amount')
  invoice_total_qty=0
  invoice_amount=0

  for i in  invoicedata:
    invoice_total_qty += i['quantity']
    invoice_amount += i['price'] *i['quantity']
  invoice_data= list(invoicedata)
  for i in invoice_data:
    i['invoice_date'] = reformat_date(i['invoice_date'] )
  print(f'***invoicedata  ****: {invoice_data}')  
  return invoice_data,invoice_total_qty,invoice_amount

def save_invoice(request):  
  if request.method == 'POST':
    form = InvoiceForm(request.POST or None)
    if form.is_valid():
      print(f'form is valid***')
      sid =  request.POST.get('stuid')
      amount = int( request.POST.get('quantity')) * int(request.POST.get('price'))
      if sid=='':
        s=Invoice(user=request.user,
          customer=Customer.objects.get( id=request.POST.get('customer')),
          description= request.POST.get('description'),
          quantity = request.POST.get('quantity'),
          price = request.POST.get('price'),
          amount=amount
          
          )
      else:  
        s=Invoice(id=sid,
          user=request.user, 
          customer=Customer.objects.get(id=request.POST.get('customer')),
          description= request.POST.get('description') , 
          quantity = request.POST.get('quantity'),
          price = request.POST.get('price'),
          amount=amount
          )
      
      s.save()
      invno=0
      invoice_data,invoice_total_qty,invoice_amount =data_list(request,invno)
      return JsonResponse({
        'status':'Success',
        'invoice_data':invoice_data,
        'invoice_total_qty':invoice_total_qty, 
        'invoice_amount':invoice_amount})
    
    else:
      return JsonResponse({'status':'Invalid Form',})
    

def invoice_edit(request):
  if request.method == "POST":  
    id = request.POST.get("sid")
    invoice = Invoice.objects.get(pk=id)

    categ_data = {'status':'Success','id':invoice.id, 'description': invoice.description,'customer_name':invoice.customer.name}
    print(f'*** edit {invoice.customer.name}' )
    return JsonResponse(categ_data)
  else:
    categ_data = {'status':'Failed'}
    return JsonResponse(categ_data)
def invoice_delete(request):
  if request.method == "POST":  
    id = request.POST.get("sid")
    invoice = Invoice.objects.get(pk=id)
    print(f'record to delete : {invoice}')
    invoice.delete()

    invoicedata =   Invoice.objects.filter(user=request.user, invoice_no = 0).values('id','customer','customer__name','description','invoice_date','quantity', 'price', 'amount')
          
    invoice_total_qty=0
    invoice_amount=0

    for i in  invoicedata:
      invoice_total_qty += i['quantity']
      invoice_amount += i['price'] *i['quantity']



    return JsonResponse({"status": 1, 'invoice_total_qty':invoice_total_qty,'invoice_amount':invoice_amount
                         
                         })
  else:
    return JsonResponse({"status": 0})  

def date_formatting(request):
  card_title='date formatting'
  mdata= Invoice.objects.filter(user=request.user).values('id','customer','customer__name','description','invoice_date','quantity','price','amount')
  invoice_db= list(mdata)  
  print(f'invoice_db : {invoice_db}')
  for i in invoice_db:
    i['invoice_date'] = reformat_date(i['invoice_date'] )
  date_sample1_form= Date_Sample1()
  context={'card_title':card_title,
           'invoice_db':invoice_db, 
           "date_sample1_form": date_sample1_form}
  return render(request,'app_invoice/date-formatting.html', context)

def get_format_date(request):
  newformat = 'kk'
  mresponse={'status':'Success', 'newformat':newformat}
  return JsonResponse()

def reformat_date(val):
  print(f'reformatting val: {val}')
  #  abbreviated month %b
  #  abbreviated full month %B
  
  
  # val = val.strftime("%B %d, %Y, %H:%M ")

  # val = val.strftime("%B %d, %Y, %I:%M %p")

  val = val.strftime("%Y/%m/%d, %I:%M %p")

  return val

def read_invoice_file (request):
  print(f'***read invoice file ')
  mdata = Invoice.objects.filter(user=request.user).values('id','customer','customer__name','description','invoice_date','quantity','price','amount') 
  invoice_data= list(mdata)  
  print(f'mdata as list  : {invoice_data}')
  for i in invoice_data:
    i['invoice_date'] = reformat_date(i['invoice_date'] )
  return JsonResponse({'status':'Success','invoice_data':invoice_data})

def dynamic_form_input(request):
  title = 'Dynamic Form Input'
  context={'title': title}
  return render(request,'app_invoice/dynamic-form-input.html', context)

def get_invoice_x():
  qs =Ref_Table.objects.filter(reference='Sales Invoice').values('ref_no')
  prev_val = qs[0]['ref_no']
  print(f'prev_val  :   {type(prev_val)} , {prev_val}'  )
  Ref_Table.objects.filter(reference='Sales Invoice').update(ref_no=prev_val+1)
  newval =Ref_Table.objects.filter(reference='Sales Invoice').values('ref_no')
  print(f' prev_val{prev_val}, newval: {newval}')
  return prev_val


def get_invoice():
  '''get the value of  invoice  in reference table'''
  prev_val =Ref_Table.objects.filter(reference='Sales Invoice').values('ref_no')[0]['ref_no']
  print(f"prev_val : {type(prev_val)} ")

  '''increment the value for the next invoice '''
  Ref_Table.objects.filter(reference='Sales Invoice').update(ref_no=prev_val+1)

  newval =Ref_Table.objects.filter(reference='Sales Invoice').values('ref_no')[0]['ref_no']

  print(f"newval : {type(newval)} , {newval}")
  return newval

def put_invoice(request,new_invoice):
  ''' 
  update the invoice number if user  and invoice value is 0
  '''
  Invoice.objects.filter(user=request.user,invoice_no = 0).update(invoice_no=new_invoice)

  qs_sum =Invoice.objects.filter(user=request.user, invoice_no = new_invoice).aggregate(Sum('quantity') , Sum('amount') ) 

  # print(f"getting the summ of total invoice :\n{qs_sum} \n sum quantity: {qs_sum['quantity__sum'] } \n sum amount : {qs_sum['amount__sum']}")


  InvoiceSummary.objects.create(user=request.user,invoice_no =new_invoice , total_quantity = qs_sum['quantity__sum'] ,total_amount=qs_sum['amount__sum'])




  

def create_an_invoice(request):
  '''get the invoice no from the reference file '''
  new_invoice = get_invoice()

  put_invoice(request,new_invoice)

  # joven from appsample

  print_invoice(request,new_invoice)

  
  
  
  invno = 0
  invoice_data,invoice_total_qty,invoice_amount = data_list(request,invno)


  return JsonResponse({'status':'Success',
                       'message':'invoice printed', 
                       'new_invoice': new_invoice,
                       'invoice_data':invoice_data,
                       'invoice_total_qty':invoice_total_qty,
                       'invoice_amount':invoice_amount
                      
                       })
