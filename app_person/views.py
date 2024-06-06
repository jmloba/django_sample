from django.shortcuts import get_object_or_404, redirect, render
from .models import Person, Country, City
from tablib import Dataset
from .resources import CountryResource, CityResource
from .forms import PersonCreationForm


# Create your views here.
def person_main(request):
  persons= Person.objects.all()

  form = PersonCreationForm()
  if request.method == 'POST':
      form = PersonCreationForm(request.POST)
      if form.is_valid():
          form.save()
          return redirect('app_person:person-main')  
      else:
         print(' **** person form Invalid')

  context={'form':form, 'persons':persons}
  return render(request,'app_person/person_main.html', context) 



def person_update_view(request, pk):
    person = get_object_or_404(Person, pk=pk)
    form = PersonCreationForm(instance=person)
    if request.method == 'POST':
        form = PersonCreationForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('person_change', pk=pk)
    context={'form':form}    
    return render(request, 'app_person/person_main.html', context)


# AJAX
def load_cities(request):
    country_id = request.GET.get('country_id')
    cities = City.objects.filter(country_id=country_id).all()
    return render(request, 'app_person/city_dropdown_list_option.html', {'cities': cities})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)

   
def import_file_excel(request):
  print('import excel')
  if request.method =='POST':
    country_resource = CountryResource()
    dataset = Dataset()
    new_countrys = request.FILES['myfile']
    imported_data = dataset.load(new_countrys.read(),format='xlsx')
    for data in imported_data:
      value= Country(
        name=data[0],
        code = data[1],
        iso_code = data[2],
        tld =  data[3],
        region = data[4]
      )
      value.save()

  return render(request,'app_person/form.html')

   
def import_cities_file_excel(request):
  print('import excel')
  if request.method =='POST':
    city_resource = CityResource()
    dataset = Dataset()
    new_cities = request.FILES['myfile']
    imported_data = dataset.load(new_cities.read(),format='xlsx')
    for data in imported_data:
      value= City(
        country=data[0],
        name = data[1],
        province = data[2],
      )
      value.save()

  return render(request,'app_person/form-cities.html')



