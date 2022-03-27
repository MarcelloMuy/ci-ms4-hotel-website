''' Imported Modules '''
from django.shortcuts import render, redirect
from .models import Booking
from .forms import BookingForm


def display_bookings(request):
    ''' Function to render Bookings objects in mybookings.html template '''
    mybookings = Booking.objects.all()
    context = {
        'mybookings': mybookings
    }
    return render(request, '../templates/mybookings.html', context)


def display_home(request):
    ''' Function to display home page'''
    return render(request, '../templates/index.html')


def display_booknow(request):
    ''' Function to display booknow page'''
    if request.method == 'POST':  # Look for POST method only
        form = BookingForm(request.POST)
        if form.is_valid():  # Check if form is valid
            form.save()
            return redirect('/mybookings/')
    form = BookingForm()
    context = {
        'form': form
    }
    return render(request, '../templates/booknow.html', context)
