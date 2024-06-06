from django.urls import path,re_path
from . import views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

app_name='app_invoice'
urlpatterns=[
      path('create_invoice/',views.invoice_create , name ='invoice-create'),
      
      path('search-desc/',views.search_desc , name ='search-desc'),

      
      path('save_invoice/',views.save_invoice , name ='save-invoice'),
      path('invoice-edit/',views.invoice_edit , name ='invoice-edit'),
      path('invoice-delete/',views.invoice_delete , name ='invoice-delete'),

      path('date-formatting/',views.date_formatting , name ='date-formatting'),
      
      path('get-format-date/',views.get_format_date , name ='get-format-date'),
      
      path('read-invoice-file/',views.read_invoice_file , name ='read-invoice-file'),

      path('dynamic-form-input/',views.dynamic_form_input , name ='dynamic-form-input'),
      
      
      path('create-an-invoice/',views.create_an_invoice, name ='create-an-invoice'),


]

      
