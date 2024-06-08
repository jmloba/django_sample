# python manage.py runscript orm_script

from app_invoice.models import Invoice, Ref_Table
from datetime import datetime
from django.db.models import Sum, Q
from django.db import connection
from sql_metadata import Parser


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
  

  


 

  
def run():
  
  # replace_invoice()
  #ref_table_view()
  invoice_no = 4
  create_simple_table(invoice_no)


  
  
  
    




  