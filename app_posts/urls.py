from django.urls import path,re_path
from . import views

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings


app_name='app_posts'

urlpatterns=[
    path('posts/',views.posts_list_and_create, name ='posts'),
  

    path('hello-world/',views.hello_world_view, name ='hello-world'),

    # path('load-post-data/',views.load_posts_data_view, name ='posts'),  

]
