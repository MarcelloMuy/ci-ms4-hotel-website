from django import forms
from .models import Booking


class DateInput(forms.DateInput):
    input_type = 'date'


class BookingForm(forms.ModelForm):
    '''comment'''
    class Meta:
        model = Booking
        fields = ['check_in_date', 'number_of_nights', 'number_of_guests', 'type_of_room', 'user']
        widgets = {
            'check_in_date': DateInput(),
        }
        
