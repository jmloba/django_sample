from django.contrib import admin
from .models import Student, Course

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
  list_display=('name',)
  ordering=('name',)
  # list_editable =('name',)
  filter_horizontal=()
  list_filter =()
  fieldsets=()

class StudentAdmin(admin.ModelAdmin):
  list_display=('firstname','lastname', 'course','email','date_created')
  ordering=('firstname','lastname')
  list_editable =('email',)
  filter_horizontal=()
  list_filter =()
  fieldsets=()    

admin.site.register(Course, CourseAdmin)
admin.site.register(Student, StudentAdmin)