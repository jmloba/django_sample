from django.contrib import admin
from .models import Invoice,Ref_Table,InvoiceSummary

# Register your models here.
class InvoiceAdmin(admin.ModelAdmin):
  list_display=('user','customer','invoice_no','invoice_date','itemnumber','description','quantity','price','amount')
  ordering=('-invoice_no','amount')
  list_editable =('invoice_no','invoice_date','itemnumber','description','quantity','price','amount')
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

class InvoiceSummaryAdmin(admin.ModelAdmin):
  list_display=('user','customer','invoice_no','invoice_date','total_quantity','total_amount','invoice_date')

  ordering=('-invoice_date','invoice_no')
  list_editable =('invoice_date','invoice_no',)
  filter_horizontal=()
  list_filter =()
  fieldsets=()


admin.site.register(Invoice, InvoiceAdmin)  
admin.site.register(Ref_Table, Ref_TableAdmin)  
admin.site.register(InvoiceSummary, InvoiceSummaryAdmin)  