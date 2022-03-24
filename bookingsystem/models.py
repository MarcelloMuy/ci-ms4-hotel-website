''' Modules from django '''
from django.db import models
from django.contrib.auth.models import User
from datetime import date


class Bookings(models.Model):
    ''' Model for user bookings '''
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_bookings")
    created_on = models.DateTimeField(auto_now_add=True)
    number_of_guests = models.IntegerField(default=1)
    check_in_date = models.DateField(default=date.today)
    number_of_nights = models.IntegerField(default=1)
    TYPE_OF_ROOM_CHOICES = [
        ('Sgl', 'Single Room'),
        ('Dbl', 'Double Room'),
        ('Fam', 'Family Room'),
    ]
    types_of_room = models.CharField(max_length=15, choices=TYPE_OF_ROOM_CHOICES, blank=False, default='Single')
    
    def __str__(self):
        return str(self.check_in_date)
    class Meta:
        ordering = ['check_in_date']
