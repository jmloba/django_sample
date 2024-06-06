
from django import forms
from .models import  Course, Product, Task,Order, Customer

class CourseForm(forms.Form):
    course = forms.CharField(label="Course", max_length=100)

class ProductForm(forms.ModelForm)  :  
    class Meta:
        model = Product
        fields=('name', 'description','category', 'price')


class TaskForm(forms.ModelForm)  :  
    class Meta:
        model = Task
        fields=('body',)     

class  OrderForm(forms.ModelForm):         
    class Meta:
        model = Order
        fields='__all__'


class  CustomerForm(forms.ModelForm):         
    class Meta:
        model = Customer
        fields='__all__'
        exclude = ['user']

