from django.urls import path,re_path
from . import views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings


app_name='app_hr'
urlpatterns=[
    path('department_list/',views.department_list , name ='department-list'),
    
    path('department_create/',views.department_create , name ='department-create'),
     
    path('phone_add/',views.phone_add, name ='phone-add'),
    #employee
        


    path('employee_profile/<pk>/',views.employee_profile, name ='employee-profile'),

    path('crispy_add_photo/',views.crispy_add_photo, name ='crispy-add-photo'),

    path('create_employee/',views.create_employee, name ='create-employee'),

    
    path('add_employee/',views.add_employee, name ='add-employee'),
    

    
    re_path(r'^employee_delete/$', views.employee_delete ,name='employee-delete'),

    re_path(r'^employee-delete-with-file/$', views.employee_delete_with_file ,name='employee-delete-with-file'),

    re_path(r'^context_processor/$', views.context_processor ,name='context-processor'),

    re_path(r'^print-profile/$', views.print_profile ,name='print-profile'),
    re_path(r'^password-protected/$', views.password_protected ,name='password-protected'),
            
        
  
]
urlpatterns+= staticfiles_urlpatterns()
urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)