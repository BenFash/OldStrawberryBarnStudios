from django import forms
from .models import Reservation
from django.core.exceptions import ValidationError
from phonenumber_field.formfields import PhoneNumberField
import datetime

class ReservationForm(forms.ModelForm):
    guest_phone = PhoneNumberField(region="GB", required=False, label='Guest Phone')

    class Meta:
        model = Reservation
        fields = ['guest_name', 'guest_email', 'check_in', 'check_out', 'num_guests', 'dog', 'vehicle', 'guest_info']
        widgets = {
            'check_in': forms.DateInput(attrs={'type': 'date'}),
            'check_out': forms.DateInput(attrs={'type': 'date'}),
            'dog': forms.CheckboxInput(),
            'vehicle': forms.CheckboxInput(),
            'num_guests': forms.NumberInput(attrs={'min': 1, 'max': 2}),
        }

    def clean_num_guests(self):
        num_guests = self.cleaned_data.get('num_guests')
        if num_guests > 2:
            raise ValidationError('The number of guests cannot exceed 2.')
        return num_guests

    def clean_check_in(self):
        check_in = self.cleaned_data.get('check_in')
        if not check_in:
            return check_in

        if check_in.weekday() not in [0, 4]:  # Monday is 0, Friday is 4
            raise ValidationError('Check-in date must be either a Monday or a Friday.')
        return check_in

    def clean(self):
        cleaned_data = super().clean()
        check_in = cleaned_data.get('check_in')
        check_out = cleaned_data.get('check_out')

        if check_in and check_out:
            nights_stay = (check_out - check_in).days
            if check_in.weekday() == 0:  # Monday
                valid_nights = [4, 7]
            elif check_in.weekday() == 4:  # Friday
                valid_nights = [2, 3, 7]
            else:
                valid_nights = []

            if nights_stay not in valid_nights:
                raise ValidationError('Invalid number of nights for the selected check-in date.')

        return cleaned_data

