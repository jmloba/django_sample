from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.contrib.auth.tokens import default_token_generator  




# UTILS
from app_accounts.utils import detectUser, send_verification_email
from django.utils.http import  urlsafe_base64_decode 

#TABLES
from app_sample.models import Customer
from .models import UserAccess

#forms
from .forms import CreateUserForm, UserAccessForm, UserProfileForm 
from .decorators import unauthenticated_user,allowed_users,admin_only

# Create your views here.
@unauthenticated_user
def register_view(request):
  form = CreateUserForm()
  profile_form = UserProfileForm(request.POST)
  useraccessform = UserAccessForm(request.POST) 
  if request.method =='POST':
    form = CreateUserForm(request.POST)
    if form.is_valid():
      user=form.save()
      '''
      # useraccess = useraccessform.save(commit=False)
      # useraccess.user = user
      # useraccess.save()

      # profile = profile_form.save(commit=False)
      # profile.user= user 
      # profile.save()

            '''


     
      # put this as signal
      '''
      user.groups.add(group)
      Customer.objects.create(user = user, name=user.username)

      '''


      m_user = form.cleaned_data.get('username')
      messages.success(request,'Successfully registered : ' + m_user)
      return redirect('app_accounts:login-view')




  context = { 'form':form}
  return render(request,'app_accounts/register.html', context )  
@unauthenticated_user
def login_view(request):
  if request.method=='POST':
    username = request.POST.get('username')
    password= request.POST.get('password')
    user = authenticate(request,username = username , password= password)
    if user is not None:
      login(request,user)
      return redirect('home')
    
    else:
      messages.info(request,'Username or password is incorrect')
      
  context = { }
  return render(request,'app_accounts/login.html',context)


def logout_view(request):
  
    logout(request)
    return redirect('app_accounts:login-view')
    # return redirect('home')

def forgot_password(request):
  if request.method =='POST':
    email=request.POST['email']
    if User.objects.filter(email=email).exists():
      print(f'---->>>> email exitst')
      user=User.objects.get(email__exact=email)
      # send reset password email
      mail_subject= 'Reset Password' 
      email_template = 'app_accounts/email/reset_password_email.html'

      print('---->>>> before send verification  *************')
      send_verification_email(request,user,mail_subject,email_template)
      print('---->>>> after send verification  *************')
      messages.success(request,'We have sent you the link thru your email')
      return redirect('app_accounts:login-view')
    else:
      messages.success(request,'Account does not exist')
      return redirect('app_accounts:forgot-password') 
  
  return render(request,'app_accounts/forgot_password.html',  )    

def reset_Password(request):
  if request.method =='POST':
    password1=request.POST['password1']
    password2=request.POST['password2']
    messages.info(request,f'password1:{password1}  password2 :{password2} ')
    if password1==password2:
      pk = request.session.get('uid')
      user =User.objects.get(pk=pk)
      user.set_password(password1)
      user.is_active = True
      user.save()
      messages.success(request,'Password reset successfull')
      return redirect('app_accounts:login-view')
    else:
      messages.success(request,'Password does not match')
      return redirect('app_accounts:reset_Password')

    #   user.is_active = True
    #   user.save()
    #   messages.success(request,'Congratulations, Your account is now active')
    #   return redirect('myAccount')
  return render(request,('app_accounts/reset_Password.html'))

def reset_Password_validate(request, uidb64, token):
  try: 
    ''' note uid is a primary key from the link'''
    uid =  urlsafe_base64_decode(uidb64).decode()
    user =User._default_manager.get(pk=uid)
  except(TypeError,ValueError,OverflowError,User.DoesNotExist):
    user=None  

  if user is not None and default_token_generator.check_token(user,token):
    request.session['uid']= uid
    messages.info(request,'Please reset you password')


    return redirect('app_accounts:reset_Password')
  else:
    messages.error(request,'This link has been expired')
    return redirect('app_accounts:login-view')
