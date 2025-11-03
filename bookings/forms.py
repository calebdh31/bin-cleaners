from django import forms
from .models import Booking



class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['date', 'address', 'service_type']
        widgets = {
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            ),
        }


