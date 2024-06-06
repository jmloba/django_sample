
from .models import  Course , Product,Task, Customer, Order

# from app_student.models import Student, Course as Student_Course

from .forms import CourseForm,ProductForm, TaskForm, OrderForm, CustomerForm
from django.http import HttpResponse, JsonResponse
from django.forms import inlineformset_factory
from django.shortcuts import redirect, render
from .filters import OrderFilter
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from app_accounts.decorators import unauthenticated_user, allowed_users,admin_only


# Create your views here.
def topics(request):
  return render(request,'app_sample/topics.html'  )


def bootstrap_box(request):
  return render(request,'app_sample/bootstrap-box.html'  )

def topics(request):
  return render(request,'app_sample/topics.html'  )

# @login_required(login_url='accounts:login-view')
# # @allowed_users(allowed_roles=['customer'])
# def dashboard(request):
 
#   context={}
#   return render(request,'app_sample/dashboard.html',context )

# @login_required(login_url='accounts:login-view')
# @allowed_users(allowed_roles=['customer'])
# def user_page(request):
#   orders = request.user.customer.order_set.all()
  
#   total_orders = orders.count()
#   delivered = orders.filter(status='Delivered').count()
#   pending  = orders.filter(status='Pending').count()
  

#   context={"orders": orders,'total_orders':total_orders,'delivered':delivered, 'pending':pending }
  
#   return render(request, 'app_sample/user.html', context)

@login_required(login_url='accounts:login-view')
def sample_course(request):
  courses = Course.objects.all()
  if request.method == 'POST':
    form_course = CourseForm(request.POST)

    if form_course.is_valid():
      course = form_course.cleaned_data['course']
      instance = Course.objects.create(course=course)
      instance.save()
      return redirect('app_sample:sample_course') 
    else:
      return redirect('app_sample:sample_course')  

  else:  
    form_course = CourseForm()
  context={'form_course':form_course,"courses":courses}
  return render(request,'app_sample/sample_course.html', context )  

# @login_required(login_url='accounts:login-view')
# def TaskList(request):
#   if request.method =='GET':
#     tasks=Task.objects.all().order_by('-body')
#     form = TaskForm()
#     context={'tasks':tasks, 'form':form}
#     return render(request,'app_sample/task-index.html', context )
  
#   if request.method == 'POST':
#     task = Task.objects.create(
#       body=request.POST.get('body')
#     )
#     task.save()
#     return redirect('app_sample:tasks')
  
# @login_required(login_url='accounts:login-view')  
# def TaskDetail(request,pk=None):
#   if request.method =='GET':
#     form = TaskForm()
#     task = Task.objects.get(id=pk)
#     context = {'task':task, 'form': form}
#     return render(request,'app_sample/task-detail.html', context)
#   if request.method =='POST':
#     task = Task.objects.get(id=pk)
#     task.body = request.POST.get('body')
#     task.save()
#     return redirect('app_sample:tasks')
  
# @login_required(login_url='accounts:login-view')  
# def TaskDelete(request,pk):
#   task = Task.objects.get(id=pk)
#   if request.method =='POST':
#     task.delete()
#     return redirect('app_sample:tasks')
#   context = {'task': task}
#   return render(request,'app_sample/task-delete.html', context)


# @login_required(login_url='accounts:login-view')
# @allowed_users(allowed_roles=['admin'])
# def product_view(request):
#   products = Product.objects.all
#   context = {'products':products}
#   return render(request,'app_sample/products.html', context)


@login_required(login_url='accounts:login-view')
@allowed_users(allowed_roles=['admin'])
def customer_view(request, pk=None):
  customer = Customer.objects.get(id=pk)
  orders = customer.order_set.all()  # child

  orders_count= orders.count()
  myFilter = OrderFilter(request.GET, queryset=orders)
  orders = myFilter.qs


  context = {'customer':customer, 'orders':orders, 'orders_count': orders_count,'myFilter':myFilter}

  return render(request,'app_sample/customer.html', context)  

# @login_required(login_url='accounts:login-view')
# @allowed_users(allowed_roles=['admin'])
# def order_create(request, pk = None):
#   OrderFormSet = inlineformset_factory(Customer,Order, fields=('product','status', 'notes'),)

#   customer = Customer.objects.get(id=pk)
#   '''this includes with the existing record'''
#   formset =OrderFormSet (instance = customer) 
#   '''this excludes the existing record'''
#   formset =OrderFormSet (queryset=Order.objects.none(),
#                          instance = customer) 

#   # form = OrderForm( initial = {'customer':customer,})

#   if request.method=='POST':
#     # print(f'posted data : {request.POST}')
#     # form = OrderForm(request.POST)
#     formset = OrderFormSet(request.POST, instance = customer)
#     if formset.is_valid():
#       formset.save()
#       return redirect('home')
#   else:
#     form = OrderForm()
#   context ={'formset':formset,'customer':customer}
#   return render(request,'app_sample/order-form.html', context)  

# @login_required(login_url='accounts:login-view')
# def order_update(request,pk=None):
#   order = Order.objects.get(id=pk)
#   form = OrderForm(instance = order) # prefill the form 

#   if request.method=='POST':
#     # print(f'posted data : {request.POST}')
#     form = OrderForm(request.POST, instance=order)
#     if form.is_valid():
#       form.save()
#       return redirect('home')

#   context ={'form':form}
#   return render(request,'app_sample/order-form.html', context)  

# @login_required(login_url='accounts:login-view')
# @allowed_users(allowed_roles=['admin'])
# def order_delete(request,pk=None):
#   order = Order.objects.get(id=pk)
#   print(f'order to delete : {order}')
#   if request.method=='POST':
#     order.delete()  
#     return redirect('home')
#   context ={'item':order, }
#   return render(request,'app_sample/order-delete.html', context)  


# # def order_list(request):
# #     filter = OrderFilter(request.GET, queryset=Product.objects.all())
# #     return render(request, 'my_app/template.html', {'filter': filter})
# @login_required(login_url='accounts:login-view')
# @allowed_users(allowed_roles=['customer','admin'])
# def account_setting(request):
#   customer = request.user.customer

#   form = CustomerForm(instance=customer)
#   if request.method=='POST':
#     form = CustomerForm(request.POST, request.FILES, instance = customer)
#     if form.is_valid():

#       form.save()

#   context={'form':form}
#   return render(request,'app_sample/account-setting.html', context)  
 
# def date_sample(request):
#   context={}
#   return render(request,'app_sample/date-sample.html', context)  

# # danny
# def read_text_file(request):
#   context={}
#   return render(request,'app_sample/read-text-file.html', context)  

# def  foreign_key_samples(request):
#   course_list = Student_Course.objects.all()
#   students= Student.objects.all()

#   print( f'students :{students} ')


#   context={'course_list': course_list, 'students':students}
#   return render(request,'app_sample/foreignkey-sample.html', context)  
# def select_option(request):
#   context={}
#   return render(request,'app_sample/select-option.html', context)    

