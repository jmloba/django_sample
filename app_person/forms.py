from django import forms
from .models import Person, City, Country



class PersonCreationForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        '''override the settings'''
        super().__init__(*args, **kwargs)

        self.fields['country'].queryset = Country.objects.filter(active = True)

        ''' initializing city as None'''
        self.fields['city'].queryset = City.objects.none()
        # self.fields['city'].queryset = City.objects.all()

        if 'country' in self.data:
            try:
                country_id = int(self.data.get('country'))
                self.fields['city'].queryset = City.objects.filter(country_id=country_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['city'].queryset = self.instance.country.city_set.order_by('name')    


