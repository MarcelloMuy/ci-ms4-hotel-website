''' Imported Modules '''
from datetime import date
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Booking
from .forms import BookingForm


def display_bookings(request):
    '''
    Function to render Bookings objects in mybookings.html template 
    mybookings - Filter objects by user id
    past_bookings - Filter objects by check in date older than today
    upcoming_bookings - Filter objects by check in date greater than 
    or equal to today
    '''
    mybookings = Booking.objects.filter(
        user=request.user.id
        ).all()
    past_bookings = mybookings.filter(
        check_in_date__lt=date.today()
        ).all()
    upcoming_bookings = mybookings.filter(
        check_in_date__gte=date.today()
        ).all()
    context = {
        'mybookings': mybookings,
        'past_bookings': past_bookings,
        'upcoming_bookings': upcoming_bookings,
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
            form.instance.user = request.user  # Book as authenticated user
            form.save()
            return redirect('/thankyou/')
    form = BookingForm()
    context = {
        'form': form
    }
    return render(request, '../templates/booknow.html', context)


def thank_you_message(request):
    ''' Function to display thank you page/message '''
    return render(request, '../templates/thankyou.html')


def update_booking(request, booking_id):
    '''Function to edit bookings'''
    # Get object with specific id or return 404 error
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':  # Look for POST method only
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():  # Check if form is valid
            form.save()
            messages.success(request, 'Thank you for updating your booking!')
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
    messages.success(request, 'Your booking has been cancelled')
    return redirect('/mybookings/')
