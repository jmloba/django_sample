# python manage.py runscript orm_script

from app_invoice.models import Invoice, Ref_Table
from datetime import datetime
from django.db.models import Sum, Q

def reformat_date(val):
  result = 'val'
  return result

def reformat_date(val):
  print(f'reformatting val: {val}')
  # val = val.strftime("%B %d, %Y %H:%M")

  val = val.strftime('%a %H:%M  %d/%m/%y')
  return val

def replace_invoice():

  invoices = Invoice.objects.values()
  print(f' 1. print invoices *** : \n\n {invoices}\n\n' )
  #to list 
  '''
  for i in invoices:
    print(f'line : { i["description"] }' )
  '''
  
  # to add in a list
  ''' for i in invoices:
    i['phone']= 1
  print( invoices)
  '''

  # to replace a value 
  '''
  for i in invoices:
    i['description']= 'me myself'
  print( invoices)    
  '''

  # # replace the value of date
  # for i in invoices:
  #   i['invoice_date']= reformat_date(i['invoice_date'])
  # print( invoices)    
def ref_table_view():

  qs =Ref_Table.objects.filter(reference='Sales Invoice').values('ref_no')
  prev_val = qs[0]['ref_no']
  print(f'prev_val  :   {type(prev_val)} , {prev_val}'  )
  Ref_Table.objects.filter(reference='Sales Invoice').update(ref_no=prev_val+1)
  newval =Ref_Table.objects.filter(reference='Sales Invoice').values('ref_no')
  print(f' prev_val{prev_val}, newval: {newval}')

def  invoice_query(invno):
  qs= Invoice.objects.filter(invoice_no=invno).aggregate(qtysum=Sum('quantity'),qtyamt=Sum('amount'))
  print(qs)
  print(qs['qtysum'],qs['qtyamt'])
  


def run():
  # replace_invoice()
  #ref_table_view()
  invoice_no = 64
  invoice_query(invoice_no)

  
  
  
    




  