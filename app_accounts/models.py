from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  bio = models.TextField(max_length=2000,blank=True)
  avatar = models.ImageField(default='avatars/avatar-default.jpg', upload_to='avatars')
  updated = models.DateTimeField(auto_now=True)
  created = models.DateField(auto_now_add=True)


  location = models.CharField(max_length=30, null=True, blank=True)
  age = models.IntegerField(default=0, null=True, blank=True)
  def __str__(self):
    return str(self.user.username)
  

  
class UserAccess(models.Model):
  user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE)
  article_create = models.BooleanField(default=False)
  article_delete = models.BooleanField(default=False)
  programmer_access=models.BooleanField(default=False)
  todo_access_all = models.BooleanField(default=False)
  todo_rights = models.BooleanField(default=False)

  # location=models.CharField(max_length=30, null=True, blank=True)

  # age = models.IntegerField(default=0)
  created_at = models.DateTimeField(auto_now_add=True)
  modified_at = models.DateTimeField(auto_now=True)
  

  def __str__(self):
    return self.user.username
  