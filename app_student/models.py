
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Course(models.Model):
  name = models.CharField(max_length=50)
  def __str__(self):
    return str(self.name)
  
class Student(models.Model):
  firstname= models.CharField(max_length=30)
  lastname= models.CharField(max_length=30)
  course = models.ForeignKey(Course,on_delete=models.PROTECT,blank=True, null=True)
  email= models.EmailField(max_length=50, blank=True, null=True)
  date_created = models.DateTimeField(auto_now_add=True, null=True)
  date_updated = models.DateTimeField(auto_now=True, null=True)


  def __str__(self):
    return self.firstname+' '+self.lastname

