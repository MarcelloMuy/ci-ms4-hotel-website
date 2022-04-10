''' Imported Modules '''
from datetime import date, datetime
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
        # Check if check-in date is at least 1 day from booking date
        # and show an error message
        date_choice = request.POST['check_in_date']
        if datetime.strptime(date_choice, '%Y-%m-%d') < datetime.today():
            messages.error(
                request,
                'The check-in date must be from tomorrow onwards!')
            return redirect('/booknow/')
        # Check if nunber of guests is less than 1 or
        # bigger than 15 and show an error message
        guests_choice = int(request.POST['number_of_guests'])
        if guests_choice < 1 or guests_choice > 15:
            messages.error(
                request,
                'You can only make a booking for up to 15 people!')
        nights_choice = int(request.POST['number_of_nights'])
        # Check if nunber of nights is less than 1 or
        # bigger than 30 and show an error message
        if nights_choice < 1 or nights_choice > 30:
            messages.error(
                request,
                'You can only make a booking for up to 30 nights!')
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


def our_rooms(request):
    ''' Function to display our rooms page '''
    return render(request, '../templates/ourrooms.html')


def update_booking(request, booking_id):
    '''Function to edit bookings'''
    # Get object with specific id or return 404 error
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':  # Look for POST method only
        # Check if check-in date is at least 1 day from booking date
        # and show an error message
        date_choice = request.POST['check_in_date']
        if datetime.strptime(date_choice, '%Y-%m-%d') < datetime.today():
            messages.error(
                request,
                'The check-in date must be for at least '
                'one day from the booking date')
            form = BookingForm(instance=booking)  # Prepopulate form
            context = {
                'form': form
            }
            return render(request, '../templates/updatebooking.html', context)
        # Check if nunber of guests is less than 1 or
        # bigger than 15 and show an error message
        guests_choice = int(request.POST['number_of_guests'])
        if guests_choice < 1 or guests_choice > 15:
            messages.error(
                request,
                'You can make a booking for 1 to 15 people only!')
        nights_choice = int(request.POST['number_of_nights'])
        # Check if nunber of nights is less than 1 or
        # bigger than 30 and show an error message
        if nights_choice < 1 or nights_choice > 30:
            messages.error(
                request,
                'You can make a booking for up to 30 days only!')
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
