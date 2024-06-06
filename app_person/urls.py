from django.urls import path,re_path
from . import views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
app_name='app_person'
urlpatterns=[
  # import excel
  path('import-file-excel/',views.import_file_excel , name ='import-file-excel'),  
  path('import-cities-file-excel/',views.import_cities_file_excel , name ='import-cities-file-excel'),  

  path('person-main/',views.person_main , name ='person-main'),
    path('<int:pk>/', views.person_update_view, name='person_change'),
    path('ajax/load-cities/', views.load_cities, name='ajax-load-cities'), # AJAX

   
    

]
  