
from django.contrib import admin
from django.urls import path, include
from . import views

app_name='main'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home , name ='home' ),    
    path('accounts/',    include('app_accounts.urls')),
    path('app_sample/',  include('app_sample.urls')),
    path('app_sales/',  include('app_sales.urls')),
]
