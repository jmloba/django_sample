

from django import forms
from .models import Invoice

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = [
            'customer','itemnumber','description','quantity','price'
        ]

class InvoiceSearchForm(forms.ModelForm):       
    class Meta:
        model = Invoice
        fields = [
          'description'
        ]

class Date_Sample1(forms.Form ):
    mydate_field = forms.DateField()



