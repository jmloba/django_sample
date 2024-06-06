
from django.contrib import admin
from  app_sales.models import GroceryMaster, GroceryCategory

class GroceryMasterAdmin(admin.ModelAdmin):
  list_display=('item_no','description','costprice','saleprice', )
  ordering=('item_no',)
  # list_editable =('item_no','description')
  filter_horizontal=()
  list_filter =()
  fieldsets=()  


class GroceryCategoryAdmin(admin.ModelAdmin):
  list_display=('name',)
  ordering=('name',)
  # list_editable =('age','location')
  filter_horizontal=()
  list_filter =()
  fieldsets=()
  
admin.site.register(GroceryMaster,GroceryMasterAdmin )
admin.site.register(GroceryCategory, GroceryCategoryAdmin)

  