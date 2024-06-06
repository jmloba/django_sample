from django.urls import include, re_path,path
from django.contrib import admin
from . import views

app_name='app_sample'

urlpatterns = [
    re_path(r'^topics/$',views.topics, name='topics'),
    re_path(r'^sample_course/$',views.sample_course, name='sample_course'),
    re_path(r'^bootstrap-box/$',views.bootstrap_box, name='bootstrap-box'),

    path('dashboard/', views.dashboard , name ='dashboard' ),

    # task class based
    path('task/', views.TaskList , name ="tasks"),

    path('tasks/<str:pk>', views.TaskDetail , name ="task-detail"),

   path('task/<str:pk>', views.TaskDelete , name ="task-delete"),
   
    path('product_view/', views.product_view , name ="products"),

    path('customer_view/<str:pk>', views.customer_view , name ="customer"),

    path('order_create/<int:pk>', views.order_create , name ="order-create"),
    path('order_update/<str:pk>', views.order_update , name ="order-update"),

    path('order_delete/<str:pk>', views.order_delete , name ="order-delete"),
    re_path(r'^user_page/$',views.user_page, name='user-page'),
    re_path(r'^account_setting/$',views.account_setting, name='account-setting'),
    
  
    # date
    re_path(r'^date_sample/$',views.date_sample, name='date-sample'),

    # learning ajax
    re_path(r'^read_text_file/$',views.read_text_file, name='reading-text-file'),

    #
    re_path(r'^foreignkey-sample/$',views.foreign_key_samples, name='working-with-foreignkey'),

    re_path(r'^select-option-sample/$',views.select_option, name='select-option'),
 






]