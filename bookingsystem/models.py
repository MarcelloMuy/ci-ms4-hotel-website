''' Modules from django '''
from django.db import models
from django.contrib.auth.models import User


class Bookings(models.Model):
    ''' Model for user bookings '''
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_bookings")
    created_on = models.DateTimeField(auto_now_add=True)
    TYPE_OF_ROOM_CHOICES = [
        ('Single','Single'),
        ('Double','Double'),
    ]
    types_of_room = models.CharField(max_length=50, choices=TYPE_OF_ROOM_CHOICES, blank=False)
    guests = models
    
    class Meta:
        ordering = ['created_on']
