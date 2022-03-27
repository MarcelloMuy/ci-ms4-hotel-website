''' Imported Modules '''
from django import forms
from .models import Booking


class DateInput(forms.DateInput):
    '''Validates as a date format'''
    input_type = 'date'


class BookingForm(forms.ModelForm):
    '''Create a Django form'''
    class Meta:
        '''Use Booking module and specific fields to create form'''
        model = Booking
        fields = [
            'check_in_date',
            'number_of_nights',
            'number_of_guests',
            'type_of_room',
            'user'
            ]
        widgets = {
            'check_in_date': DateInput(),  # Creates a datepicker in the form
        }
