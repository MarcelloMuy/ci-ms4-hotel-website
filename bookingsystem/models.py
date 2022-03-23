''' Modules from django '''
from django.db import models
from django.contrib.auth.models import User


class Bookings(models.Model):
    ''' Model for user bookings '''
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_bookings")
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']
