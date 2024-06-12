
from django.db import models

from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError

# for signals
from django.db.models.signals import pre_save,pre_delete,post_save
from django.dispatch import receiver



ext_validator =FileExtensionValidator(['png','jpg','pdf','jpeg'])

# def validate_file_mimetype(file):
#   accept = ['images/png','images/jpg', 'employee_images/png','employee_images/jpg','employee_portfolio/pdf' ]
#   file_mime_type = magic.from_buffer(file.read(1024),mime=True)

#   print(file_mime_type)

#   if (file_mime_type not in accept):
#     raise ValidationError('Unsupported file type')
   


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
  photo       =   models.ImageField(upload_to='employee_images/', blank=True, null=True)

  myportfolio = models.FileField(upload_to='employee_portfolio/', validators=[ext_validator],blank=True, null=True)

  designation =   models.CharField(max_length=100, null=True, blank=True)
  email_address = models.EmailField(max_length=100, unique=True, null=True, blank=True)

  phone_number =  models.CharField(max_length=12, blank = True, null=True)
  department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True,blank=True , related_name='employees')

  created_at =    models.DateTimeField(auto_now_add=True)
  updated_at =    models.DateTimeField(auto_now = True)

  def __str__(self) :
    return  str(self.first_name)
  
class EmployeeHistory(models.Model):

  user=models.ForeignKey(User,on_delete=models.PROTECT, null=True, blank=True)
  operation = models.CharField(max_length=15, blank=True, null=True)
  emloyee_id=models.IntegerField(null=True, blank=True, default=0)
  first_name  =   models.CharField(max_length=100,null=True, blank=True )
  last_name   =   models.CharField(max_length=100,null=True, blank=True)
  photo       =   models.ImageField(upload_to='employee_images/', blank=True, null=True)

  myportfolio = models.FileField(upload_to='employee_portfolio/', validators=[ext_validator],blank=True, null=True)

  designation =   models.CharField(max_length=100, null=True, blank=True)
  email_address = models.EmailField(max_length=100,  null=True, blank=True)

  phone_number =  models.CharField(max_length=12, blank = True, null=True)
  department = models.ForeignKey(Department, on_delete=models.PROTECT, null=True,blank=True , related_name='employeehist')

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

# @receiver(pre_save,sender=Employee,)
# def Emp_history(sender, instance, **kwargs) :  
#    print(sender.objects.get(id=instance.id).last_name)
#    print(instance.last_name)

#    s = EmployeeHistory(operation='pre_save',emloyee_id=instance.id,first_name=instance.first_name, last_name= instance.last_name,designation=instance.designation, email_address=instance.email_address,phone_number=instance.phone_number, department=instance.department ,photo=instance.photo,myportfolio=instance.myportfolio)
#    s.save()

@receiver(post_save,sender=Employee,)
def Emp_history(sender, instance, created,*args,**kwargs) :  
   print(sender.objects.get(id=instance.id).last_name)
   print(instance.last_name)

   print(f'\n\n args : {args}\n')
   print(f'\n\n kwargs : {kwargs}\n')

   if created :
      print(f'user : {instance.first_name } has just been saved')

   s = EmployeeHistory(operation='post_save',emloyee_id=instance.id,first_name=instance.first_name, last_name= instance.last_name,designation=instance.designation, email_address=instance.email_address,phone_number=instance.phone_number, department=instance.department ,photo=instance.photo,myportfolio=instance.myportfolio)
   s.save()

@receiver(pre_delete,sender=Employee,)
def Emp_history(sender, instance, **kwargs) :  
   print(sender.objects.get(id=instance.id).last_name)
   print(instance.last_name)

   s = EmployeeHistory(operation='pre_delete',emloyee_id=instance.id,first_name=instance.first_name, last_name= instance.last_name,designation=instance.designation, email_address=instance.email_address,phone_number=instance.phone_number, department=instance.department ,photo=instance.photo,myportfolio=instance.myportfolio)
   s.save()




