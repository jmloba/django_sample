from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=50,null=True,blank=True)
    code = models.CharField(max_length=30,null=True,blank=True)
    iso_code = models.CharField(max_length=10,null=True,blank=True)
    tld    = models.CharField(max_length=10,null=True,blank=True)
    region= models.CharField(max_length=30,null=True,blank=True)
    active=models.BooleanField(default=False)

    def __str__(self):
        return self.name


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE,null=True,blank=True)

    name = models.CharField(max_length=40,null=True,blank=True,)
    province = models.CharField(max_length=40,null=True,blank=True)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=124)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name
    


