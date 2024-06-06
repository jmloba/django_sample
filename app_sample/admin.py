from django.contrib import admin
from .models import Course, Product, Task, Customer, Tag, Order

# Register your models here.

class CourseAdmin(admin.ModelAdmin):
  list_display=('course',)
  ordering=('course',)
  # list_editable =('name',)
  filter_horizontal=()
  list_filter =()
  fieldsets=()

class ProductAdmin(admin.ModelAdmin):
  list_display=('name','description', 'category','price','date_created')
  ordering=('name','category')
  list_editable =('description','category', 'price')
  filter_horizontal=()
  list_filter =()
  fieldsets=()  

class CustomerAdmin(admin.ModelAdmin):
  list_display=('name','phone', 'email','date_created')
  ordering=('name','email')
  list_editable =('phone', 'email')
  filter_horizontal=()
  list_filter =()
  fieldsets=()  

class TaskAdmin(admin.ModelAdmin):
  list_display=('body', )
  ordering=('body',)
  # list_editable =('body',)
  filter_horizontal=()
  list_filter =()
  fieldsets=()    


class TagAdmin(admin.ModelAdmin):  
  list_display=('name', )
  ordering=('name',)
  # list_editable =('body',)
  filter_horizontal=()
  list_filter =()
  fieldsets=()    

class OrderAdmin(admin.ModelAdmin):  
  list_display=('customer','product' ,'date_created', 'status', 'notes')
  ordering=('customer',)
  filter_horizontal=()
  list_filter =()
  fieldsets=()    

admin.site.register(Course, CourseAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Order, OrderAdmin)