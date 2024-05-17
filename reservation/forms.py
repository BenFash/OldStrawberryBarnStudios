from django import forms
from .models import Reservation
from django.core.exceptions import ValidationError

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['room', 'guest_name', 'guest_email', 'guest_phone', 'check_in', 'check_out', 'num_guests', 'dog', 'vehicle', 'guest_info']
        widgets = {
            'check_in': forms.DateInput(attrs={'type': 'date'}),
            'check_out': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_num_guests(self):
        num_guests = self.cleaned_data.get('num_guests')
        if num_guests > 2:
            raise ValidationError('The number of guests cannot exceed 2.')
        return num_guests

    def clean_dog(self):
        dog = self.cleaned_data.get('dog')
        if dog > 1:
            raise ValidationError('The number of dogs cannot exceed 1.')
        return dog
