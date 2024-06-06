from django.urls import path,re_path
from . import views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings


app_name='app_sales'

urlpatterns=[
  
    path('sales-main/',views.sales_main , name ='sales-main'),
    #  Category    
    path('category_entry/',views.category_entry , name ='category-entry'),
    path('category_save_entry/',views.category_add_save , name ='category-save-entry'),
    path('category_edit/',views.category_edit , name ='category-edit'),
    path('category_delete/',views.category_delete , name ='category-delete'),
    #  master
    
    path('grocery-master-entry/',views.grocery_master_entry , name ='grocery-master-entry'),

    path('grocery-master-save-entry/',views.grocerymaster_save_entry , name ='grocerymaster-save-entry'),
    
    path('grocery-delete/',views.grocery_delete , name ='grocery-delete'),     

    path('grocery-master-edit/',views.grocery_master_edit , name ='grocery-master-edit'),    

]