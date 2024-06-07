
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
    path('app_invoice/',  include('app_invoice.urls')),
    path('app_student/',  include('app_student.urls')),
    path('app_person/',  include('app_person.urls')),
    path('app_hr/',  include('app_hr.urls')),
    path('app_posts/',  include('app_posts.urls')),
    path('app_booking/',  include('app_booking.urls')),
    path('app_print/',  include('app_print.urls')),
]
