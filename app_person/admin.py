from django.contrib import admin
from .models import Country, City, Person

# Register your models here.
class CountryAdmin(admin.ModelAdmin):
  list_display=('name','active','code','iso_code','tld', 'region')
  ordering=('name','iso_code')
  list_editable =('active',)
  filter_horizontal=()
  list_filter =()
  fieldsets=()  

class CityAdmin(admin.ModelAdmin):
  list_display=('country','name','province')
  ordering=('name',)
  # list_editable =('item_no','description')
  filter_horizontal=()
  list_filter =()
  fieldsets=()  

class PersonAdmin(admin.ModelAdmin)  :
  list_display=('name','country','city')
  ordering=('name',)
  # list_editable =('item_no','description')
  filter_horizontal=()
  list_filter =()
  fieldsets=()  
      
    
admin.site.register(Country,CountryAdmin )
admin.site.register(City,CityAdmin )
admin.site.register(Person,PersonAdmin )