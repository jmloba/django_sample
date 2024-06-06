from django.db import models
from django.conf import settings

# Create your models here.
class Room(models.Model):
  ROOM_CATEGORIES=(
    ('YAC','AC'),
    ('NAC','NON-AC'),
    ('DEL','DELUXE'),
    ('KIN','KING'),
    ('QUE','QUEEN'),

  )
  number= models.IntegerField()
  category = models.CharField(max_length  = 3 , choices = ROOM_CATEGORIES)
  beds=models.IntegerField()
  capacity = models.IntegerField()
  def __str__(self):
    return f'room: {self.number}, category :{self.category}, beds: {self.beds}, capacity:{self.capacity} '
  
class Booking(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  room= models.ForeignKey(Room, on_delete=models.CASCADE)
  check_in = models.DateTimeField()
  check_out = models.DateTimeField()
  def __str__(self):
    return f'user :{self.user} booked room {self.room} from {self.check_in} to {self.check_out}'
    



