from django.contrib import admin
from .models import Phone, Department, Employee,Photo

# Register your models here.


class PhoneProfileAdmin(admin.ModelAdmin):
  list_display=('user_id','phone_no')
  ordering=('phone_no',)
  # list_editable =('age','location')
  filter_horizontal=()
  list_filter =()
  fieldsets=()

class EmployeeAdmin(admin.ModelAdmin):
  list_display=('first_name','last_name','designation','email_address')
  # ordering=('last_name','first_name')
  # list_editable =('age','location')
  filter_horizontal=()
  list_filter =()
  fieldsets=()

class DepartmentAdmin(admin.ModelAdmin):
  list_display=('name',)
  ordering=('name',)
  # list_editable =('age','location')
  filter_horizontal=()
  list_filter =()
  fieldsets=()  

class PhotoAdmin(admin.ModelAdmin):
  list_display=('name','image','description')
  ordering=('name',)
  # list_editable =('age','location')
  filter_horizontal=()
  list_filter =()
  fieldsets=()  

admin.site.register(Phone,PhoneProfileAdmin)
admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Department,DepartmentAdmin)
admin.site.register(Photo,PhotoAdmin)