from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Course(models.Model):
  course = models.CharField(max_length=100, null=False, blank=False)
  def __str__(self) :
    return str(self.course)
  
class Customer(models.Model)  :
  user = models.OneToOneField(User, null=True,blank=True, on_delete=models.CASCADE)
  name=models.CharField(max_length=200, null=True)
  phone=models.CharField(max_length=200, null=True)
  email=models.CharField(max_length=200, null=True)
  profile_pic = models.ImageField(default='profile.png',null=True,blank=True)
  date_created = models.DateTimeField(auto_now_add=True, null=True)
  def __str__(self):
    return str(self.name)

class Tag (models.Model) :
  name= models.CharField(max_length=200, null = True)
  def __str__(self):
    return self.name
class Product(models.Model):
  CATEGORY=(
    ('Indoor', 'Indoor'),
    ('Out Door', 'Out Door')
  )
  name = models.CharField(max_length=200,null=True)
  description = models.CharField(max_length=200, null=True, blank=True)
  category= models.CharField(max_length=100, null=True, choices=CATEGORY)
  price =  models.FloatField(default=0, null=True)
  date_created = models.DateTimeField(auto_now_add=True, null=True)
  tags=models.ManyToManyField(Tag)
  def __str__(self):
    return f'{self.name}'

  
class Order(models.Model):
  STATUS=(
    ('Pending', 'Pending'),
    ('Out for delivery', 'Out for delivery'),
    ('Delivered', 'Delivered'),
  )
  customer =  models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
  product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
  date_created = models.DateTimeField(auto_now_add=True, null=True)
  status = models.CharField(max_length=200, null= True, choices=STATUS )
  notes = models.CharField(max_length=2000, null= True,)

  def __str__(self):
    return f'Customer: {self.customer}  Product: {self.product} {self.date_created}'


class Task(models.Model) :
  body =  models.CharField(max_length=2000)
  # date = models.DateTimeField(auto_now_add=True)
  # completed = models.BooleanField(default=False)


  def __str__(self):
    return str(self.body)

