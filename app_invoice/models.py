from django.db import models
from app_sample.models import Customer
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import date, datetime

from django.contrib.auth.models import User


# Create your models here.
class Ref_Table (models.Model):
  reference = models.CharField(max_length=20, blank=True, null=True)
  ref_no = models.IntegerField(default=0,blank=True, null=True)
  def __str__(self):
    return self.reference


class Invoice (models.Model):

  user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)                         
  customer = models.ForeignKey(Customer,on_delete=models.PROTECT, null=True, blank=True)

  invoice_no = models.IntegerField(default=0, blank=True, 
                                 null=True)

  invoice_date  = models.DateTimeField(default=datetime.now, blank=True, null=True)
  
  itemnumber = models.CharField(max_length=20, blank=True, null=True)

  description = models.CharField(max_length=50, blank=True, null=True) 
  quantity = models.IntegerField(default=1, validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ],blank=True, null=True)
  price = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True, null=True)
  amount = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True, null=True)
  def __str__(self):
    return str(self.customer)
  
class InvoiceSummary(models.Model):
  user=  user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)   

  customer = models.ForeignKey(Customer,on_delete=models.PROTECT, null=True, blank=True)

  invoice_no = models.IntegerField(default=0)

  invoice_date= models.DateTimeField(default=datetime.now, blank=True, null=True)
  total_quantity=models.IntegerField(default=0, validators=[
          MaxValueValidator(100),
          MinValueValidator(1) ],blank=True, null=True)
  total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True, null=True)    
  def __str__(self):
    return str(self.customer)
  
                      

    





