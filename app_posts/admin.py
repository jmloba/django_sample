from django.contrib import admin
from .models import Post

# Register your models here.


class PostsAdmin(admin.ModelAdmin):
  list_display=('author','body','updated','created')
  ordering=('author',)

  list_editable =('body',)
  filter_horizontal=()
  list_filter =()
  fieldsets=()

admin.site.register(Post, PostsAdmin)