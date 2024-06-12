from django import forms
from .models import Department, Phone, Employee,Photo


class DepartmentForm(forms.ModelForm):
  class Meta:
    model = Department
    fields=['name','description']
    
class PhoneForm(forms.ModelForm) :       
  class Meta:
    model = Phone
    fields=['phone_no',]
    
class EmployeeForm(forms.ModelForm):
  first_name = forms.CharField(required=True)
  class Meta:
    model=Employee
    fields=('first_name',
            'last_name',
            'photo',
            'designation',
            'email_address',
            'phone_number',
            'department','myportfolio')
    

class EmployeeForm_files(forms.ModelForm):
  first_name = forms.CharField(required=True)

  class Meta:
    model=Employee
    fields=('first_name',
            'last_name',
            'photo',
            'myportfolio',
            'designation',
            'email_address',
            'phone_number',
            'department',)
    
    widgets={
      'myportfolio': forms.FileInput(attrs={'accept':'.pdf, .png, .jpg'})
    }    
    
  def clean_first_name(self):
    first_name =self.cleaned_data.get('first_name')
    if (first_name==''):
      raise forms.ValidationError('This is a required field')
    return first_name
  
  

class PhotoForm(forms.ModelForm):
  class Meta:
    model= Photo
    fields =('image','name','description')

