from django.shortcuts import render, redirect,HttpResponse
from django.contrib import messages

from .models import Room, Booking
from app_booking.forms import AvailabilityForm

from app_booking.booking_functions.availability import check_availability

from django.views.generic import ListView, FormView

# Create your views here.
class RoomList(ListView):
  model = Room

class BookingList (ListView):
  model = Booking

class   BookingView(FormView):
  form_class = AvailabilityForm
  template_name = 'availability_form.html'

  def form_valid(self,form):
    data = form.cleaned_data
    room_list = Room.objects.filter(category=data['room_category'])
    available_rooms =[]

    for room in room_list:
      if check_availability(room, data['check_in'],  data['check_out'] ):
        available_rooms.append(room)
      print(f'for loop-> available rooms: {available_rooms}')  

    if len(available_rooms)>0:   
       
      room = available_rooms[0] 
      print (f'available rooms : *** {room}')   
      booking = Booking.objects.create(
        user = self.request.user,
        room= room,
        check_in = data['check_in'],
        check_out = data['check_out'],
      ) 
      booking.save()
      return HttpResponse(booking)
    else :
      
    
      return HttpResponse('This category of rooms are booked') 

