from django import forms
from .models import Course, Student

class Course_Form(forms.ModelForm):
  class Meta:
    model = Course
    fields = ['name']


class Student_Form(forms.ModelForm):
  class Meta:
    model = Student
    fields = '__all__'
    exclude = ('date_created', 'date_updated')
    