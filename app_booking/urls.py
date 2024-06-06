from django.urls import include, re_path,path
from django.contrib import admin

from .views import RoomList, BookingList,BookingView

app_name='app_booking'

urlpatterns = [


    path('room_list/', RoomList.as_view(), name='RoomList' ),

    path('booking_list/', BookingList.as_view(), name ='BookingList'),

    path('booking/', BookingView.as_view(), name ='bookingview'),

    ]