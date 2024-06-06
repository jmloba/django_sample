from django.db.models.signals import post_save

from app_sample.models import Customer


from django.contrib.auth.models import User, Group
from .models import UserProfile, UserAccess

from django.dispatch import receiver

def customer_profile(sender,instance,created,**kwargs):

  if created:
    group = Group.objects.get(name='customer')
    instance.groups.add(group)

    Customer.objects.create(
      user = instance, 
      name=instance.username,
      email = instance.email
      )
    print ('** profilde created ')
  else  :
    print ('** customer_profile  *** not *** created ')


post_save.connect(customer_profile, sender=User)    

@receiver(post_save,sender=User)
def post_save_create_profile(sender,instance,created,*args,**kwargs):
  print(sender)
  print(instance)
  print(created)
  if created:
    UserProfile.objects.create(user=instance)
    UserAccess.objects.create(user=instance)


