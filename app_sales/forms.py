from django import forms
from .models import GroceryCategory, GroceryMaster

class GroceryCategory_Form (forms.ModelForm):
  class Meta:
    model = GroceryCategory
    fields = ['name']


class GroceryMaster_Form(forms.ModelForm): 
    class Meta:
      model = GroceryMaster
      fields = '__all__' 

class SearchMaster_Form(forms.ModelForm):
    class Meta:
      model = GroceryMaster
      fields = ['description',]

