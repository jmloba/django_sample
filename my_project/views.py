
from app_sample.models import Customer,Order

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse

def home(request):
  customers=Customer.objects.all()
  orders=Order.objects.all()
  total_customers = customers.count

  total_orders = orders.count()
  delivered = orders.filter(status='Delivered').count()
  pending  = orders.filter(status='Pending').count()

  print (f'total_orders :{total_orders}, delivered : {delivered}, pending : {pending}')

  context = {
    'customers': customers, 'orders':orders, 'total_customers': total_customers,'total_orders': total_orders,'delivered': delivered, 'pending': pending
  }
  # context={}

  return render(request,'home.html',context )