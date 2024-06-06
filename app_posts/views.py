
from django.shortcuts import render,redirect,HttpResponse
from django.http import  JsonResponse,response
from .models import Post
from django.core import serializers

# Create your views here.
def posts_list_and_create(request):
    posts = Post.objects.all()
    context={'posts':posts}
    return render(request,'app_posts/posts.html',context )



def hello_world_view(request):
    return JsonResponse({'text':'saying hello world'})


# def load_posts_data_view(request):
#     qs = Post.objects.all()
#     data=[]
#     for obj in qs:
#         item ={
#             'id':obj.id,
#             # 'title' : obj.title,
#             # 'body' : obj.body,
#             # 'author': obj.author.user.username
#         }
#         data.append(item)
         
#     return JsonResponse({'data':data})