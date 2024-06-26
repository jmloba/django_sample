from django.shortcuts import render,redirect,HttpResponse
from django.http import  JsonResponse,response
from .forms import DepartmentForm,PhoneForm, EmployeeForm, PhotoForm, EmployeeForm_files


from .models import Department, Phone, Employee
from .print_emp_profile import print_employee_profile_now
from app_accounts.utils import is_ajax

from .serializers import ImageModeSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

# Create your views here.

def phone_add(request):
  phonelist = Phone.objects.all() 
  form = PhoneForm()
  if request.method =='POST':
    form=PhoneForm(request.POST)
    if form.is_valid():
      print(f'Request User : {request.user}')
      record = Phone.objects.filter(user_id = request.user)
      print(f'record : {record}')
      if not record:
        instance = form.save(commit=False)
        instance.user_id =request.user
        instance.save()
        return redirect('app_hr:phone-add')
      else:
        return HttpResponse('REcord exist')



  context={'phonelist':phonelist, 'form': form, }

  return render(request,'app_hr/phone_list.html', context)

def department_list(request):
  
  context={}
  return render(request,'app_hr/department_list.html', context)

def department_create(request):
  depts = Department.objects.all()
  
  form = DepartmentForm()
  if request.method =='POST':
    form=DepartmentForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('app_hr:department-create')

  context={'form':form,'depts':depts}
  return render(request,'app_hr/department_create.html', context)

def employee_profile(request,pk=None):
  employee = Employee.objects.get(id=pk)
  form= EmployeeForm(instance = employee)
  if request.method=='POST':
    form = EmployeeForm(request.POST, request.FILES, instance = employee)
    if form.is_valid():
      form.save()
  context={'form':form,"employee":employee }
  return render(request,'app_hr/employee_profile.html',context )

def create_employee(request):
  employees = Employee.objects.all()
  form =EmployeeForm(request.POST or None , request.FILES or None)

  context={'employees':employees, 'form':form}
  return render(request,'app_hr/employee-create.html', context)  


# create employee with attachement file
def get_employees(request):
  employees = Employee.objects.all()
  emp_list = list(employees)
  return employees




def add_employee(request):
  print('adding employees')
  form = EmployeeForm(request.POST or None , request.FILES or None)
  data={}
  
  if request.method=='POST':

    form = EmployeeForm(request.POST  , request.FILES )
    if form.is_valid():
      print(f' form add employee is valid form ')
      instance = form.save()

      
      data['id']=instance.id
      data['first_name']= instance.first_name
      data['last_name']= instance.last_name
      data['designation']= instance.designation
      data['department']= instance.department.name
  
      data['status']= 'ok'
      return JsonResponse(data)
    else:
      print(f'invalid form ')
      data['error'] = 'data not saved, invalid form'
      return JsonResponse(data)
 

  

      
def employee_delete(request)    :

  if request.method == "POST":  
    id = request.POST.get("sid")
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return JsonResponse({"status": 1})
  else:
    return JsonResponse({"status": 0})  
  
def employee_delete_with_file(request)    :

  if request.method == "POST":  
    id = request.POST.get("sid")
    employee = Employee.objects.get(pk=id)
    print(f'student to delete : {employee}')
    employee.delete()
    return JsonResponse({"status": 1})
  else:
    return JsonResponse({"status": 0})  

def crispy_add_photo(request):
  form = PhotoForm(request.POST or None , request.FILES or None)
  data={}
  if is_ajax(request):
    if form.is_valid():
      form.save()
      data['name']= form.cleaned_data.get('name')
      data['status']= 'ok'
      return JsonResponse(data)


  context={'form': form}
  return render(request,'app_hr/crispy_add_photo.html',context)

def context_processor(request):
  context={}
  return render(request,'app_hr/context-processor.html',context)

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def get_employee_info(empno):
  emp = Employee.objects.filter(id=empno).values('first_name','last_name','designation','email_address','phone_number','department','photo','department__name')

  photo_url= emp[0]['photo']
  print(f'photo url: {photo_url} ')

  emp1 = Employee.objects.filter(id=empno).values('photo')
  # image_url =emp1.photo.url

  print(f'--->>>>  emp1: {emp1} ')
  emp_list = list(emp) 

  return emp_list, photo_url


def password_protected(request):
  if is_ajax(request):
    response = {'status':'Success', 'Message': 'ajax request'}
    return JsonResponse(response)

def print_profile(request):
  if is_ajax(request):
      empno = int( request.POST['emp_no'])
      employee_data , photo_url= get_employee_info(empno)
      print(f'photo url : {photo_url}')


      if employee_data==None:
        print('no records')
        response = {'status':'No Value', 'Message': 'No employee record'}
        return JsonResponse(response)
      
      if  employee_data:
        mypath = 'c:/reportlab/employee_profile.pdf'
        print(f'\n\n ***** employee_data *** {employee_data}')
        
        print_employee_profile_now(employee_data,mypath,empno,photo_url)



        response = {'status':'Success', 'Message': 'invoice has been printed'}
        return JsonResponse(response)
      else  :
        mypath=''
        print('nothing to print')
        response = {'status':'No Record Found', 'Message': 'No invoice found from the table'}
        return JsonResponse(response)
    




  







