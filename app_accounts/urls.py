from django.urls import include, re_path,path
from django.contrib import admin

from . import views

app_name='app_accounts'

urlpatterns = [
    re_path(r'^register/$',views.register_view, name='register-view'),
    re_path(r'^login/$',views.login_view, name='login-view'),
    re_path(r'^logout/$',views.logout_view, name='logout-view'),


    re_path(r'^forgot_password/$',views.forgot_password, name='forgot-password'),    
    re_path(r'^reset_password/$',views.reset_Password, name='reset_Password'),

  path('reset_Password_validate/<uidb64>/<token>/', views.reset_Password_validate, name ='reset_Password_validate'), 

      
]