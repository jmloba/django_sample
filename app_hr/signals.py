from django.db.models.signals import post_save
from app_hr.models import  EmployeeHistory
from django.contrib.auth.models import User
from django.dispatch import receiver
