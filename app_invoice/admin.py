from django.contrib import admin
from .models import Invoice,Ref_Table

# Register your models here.
class InvoiceAdmin(admin.ModelAdmin):
  list_display=('user','customer','invoice_no','invoice_date','description','quantity','price','amount')
  ordering=('-invoice_no','amount')
  list_editable =('invoice_no','invoice_date','description','quantity','price','amount')
  filter_horizontal=()
  list_filter =()
  fieldsets=()

class Ref_TableAdmin(admin.ModelAdmin):
  list_display=('reference','ref_no')
  ordering=('reference',)
  list_editable =('ref_no',)
  filter_horizontal=()
  list_filter =()
  fieldsets=()

admin.site.register(Invoice, InvoiceAdmin)  
admin.site.register(Ref_Table, Ref_TableAdmin)  