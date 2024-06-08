from django.urls import path,re_path
from . import views

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings


app_name='app_print'

urlpatterns=[
    path('print-invoice/',views.print_invoice, name ='print-invoice'),
    path('reprint-invoice/',views.reprint_invoice, name ='reprint-invoice'),

    path('print-tabular/',views.print_invoice_tabular, name ='print-invoice-tabular'),


]
