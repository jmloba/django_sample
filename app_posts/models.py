from django.db import models
from django.contrib.auth.models import User
from app_accounts.models import User,UserProfile

# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=200)
  body = models.TextField()
  liked = models.ManyToManyField(User,blank=True)
  author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
  updated = models.DateTimeField(auto_now=True)
  created= models.DateTimeField(auto_now_add=True)
  def __str__(self):
    return str(self.title)


