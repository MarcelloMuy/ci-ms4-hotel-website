from django.shortcuts import render, HttpResponse
from .models import Booking



def display_bookings(request):
    mybookings = Booking.objects.all()
    context = {
        'mybookings': mybookings
    }
    return render(request, '/workspace/ci-ms4-hotel-website/templates/mybookings.html', context)

