from django.urls import include, re_path,path
from django.contrib import admin
from . import views

app_name='app_student'

urlpatterns = [
    # re_path(r'^student-menu/$',views.student_menu, name='student-menu'),
    re_path(r'^student-list/$',views.student_list, name='student-list'),
    # course

    re_path(r'^course-save-entry/$',views.course_save_entry, name='course-save'),    
    
    re_path(r'^course-edit/$',views.course_edit, name='course-edit'),   

    re_path(r'^course-delete/$',views.course_delete, name='course-delete'),   
    #student

    re_path(r'^student-save-entry/$',views.student_save_entry, name='student-save'), 
    
    re_path(r'^student-delete/$',views.student_delete, name='student-delete'),       
    re_path(r'^student-edit/$',views.student_edit, name='student-edit'),     
]