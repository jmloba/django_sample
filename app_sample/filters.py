import django_filters

from django_filters import DateFilter, CharFilter
from .models import Order

class OrderFilter(django_filters.FilterSet):
    ''' lookup gte : greater than or eqal to '''
    start_date = DateFilter(field_name = 'date_created', lookup_expr='gte')
    end_date = DateFilter(field_name = 'date_created', lookup_expr='lte')
    notes = CharFilter(field_name = 'notes', lookup_expr='icontains')

    
    class Meta:
        model = Order
        fields = '__all__'
        exclude =['customer','date_created']