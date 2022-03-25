''' Imported Modules '''
from django.shortcuts import render
from .models import Booking


def display_bookings(request):
    ''' Function to render Bookings objects in mybookings.html template '''
    mybookings = Booking.objects.all()
    context = {
        'mybookings': mybookings
    }
    return render(request, '../templates/mybookings.html', context)
