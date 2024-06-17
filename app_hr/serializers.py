from rest_framework import serializers
from rest_framework.response import Response 
from rest_framework import status 
from .models import Employee

class ImageModeSerializer(serializers.ModelSerializer) :
  class Meta:
    model = Employee
    fields='__all__'
    def get_photo_url(self,obj):
      request = self.context.get('request')
      photo_url=obj.fingerprint.url
      return request.build_absolute_uri(photo_url)


