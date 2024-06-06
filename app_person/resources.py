from import_export import resources
from .models import Country,City

class CountryResource(resources.ModelResource):
  class Meta:
    model= Country
class CityResource(resources.ModelResource):
  class Meta:
    model= City    