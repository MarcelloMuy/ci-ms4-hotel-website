''' Imported Modules '''
from django.shortcuts import render, redirect, get_object_or_404
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


def book_now(request):
    ''' Function to display booknow page and add a new booking'''
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


def update_booking(request, booking_id):
    '''Function to edit bookings'''
    # Get object with specific id or return 404 error
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':  # Look for POST method only
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():  # Check if form is valid
            form.save()
            return redirect('/mybookings/')
    form = BookingForm(instance=booking)  # Prepopulate form
    context = {
        'form': form
    }
    return render(request, '../templates/updatebooking.html', context)


def cancel_booking(request, booking_id):
    '''Function to delete bookings'''
    booking = get_object_or_404(Booking, id=booking_id)
    booking.delete()
    return redirect('/mybookings/')
