from django.db import models
from django.contrib.auth.models import User

class GroceryCategory(models.Model):
  name = models.CharField(max_length=20,blank=True, null=True )
  def __str__(self):
    return str(self.name)


class GroceryMaster(models.Model):
 
  item_no = models.CharField(max_length=20,blank=True, null=True)  
  description = models.CharField(max_length=500,blank=True, null=True)
  costprice = models.DecimalField(max_digits=8, decimal_places=2,default=0.00)
  saleprice = models.DecimalField(max_digits=8, decimal_places=2,default=0.00, blank = True, null=True)

  def __str__(self):
    return str(self.description) 


  
  

