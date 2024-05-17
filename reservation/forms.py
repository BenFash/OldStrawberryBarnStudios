from django import forms
from .models import Reservation
from django.core.exceptions import ValidationError

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['guest_name', 'guest_email', 'guest_phone', 'check_in', 'check_out', 'num_guests', 'dog', 'vehicle', 'guest_info']
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
