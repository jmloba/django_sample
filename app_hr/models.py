
from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Phone (models.Model):
  phone_no = models.CharField(max_length=20)
  user_id= models.OneToOneField(User, on_delete=models.CASCADE)
  def __str__(self):
    return self.phone_no
  
class Department(models.Model):
    name = models.CharField(max_length=255,null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.name)

  

class Employee(models.Model):
  first_name  =   models.CharField(max_length=100,null=True, blank=True )
  last_name   =   models.CharField(max_length=100,null=True, blank=True)

  photo       =   models.ImageField(upload_to='images', blank=True)

  designation =   models.CharField(max_length=100, null=True, blank=True)
  email_address = models.EmailField(max_length=100, unique=True, null=True, blank=True)

  phone_number =  models.CharField(max_length=12, blank = True, null=True)
  department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True,blank=True , related_name='employees')

  created_at =    models.DateTimeField(auto_now_add=True)
  updated_at =    models.DateTimeField(auto_now = True)

  def __str__(self) :
    return  str(self.first_name)
  

  
class Photo(models.Model):
   name = models.CharField(max_length=100)
   description = models.TextField()
   image = models.ImageField(upload_to ='images/photo/')
   created = models.DateTimeField(auto_now_add=True)
   def __str__(self):
      return str(self.name)




