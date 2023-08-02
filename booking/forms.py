from django import forms
from .models import Booking
from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput
from datetime import datetime, timedelta
from django.core.exceptions import ValidationError

# Defining choices for a dropdown in the form
PROJECTTYPE_CHOICES = [
    ('Kitchen', 'Kitchen'),
    ('Outdoor Deck', 'Outdoor Deck'),
    ('Pergola', 'Pergola'),
    ('Carport', 'Carport'),
    ('Roofing', 'Roofing'),
    ('Windows & Doors', 'Windows & Doors'),
    ('Solar Panels', 'Solar Panels'),
    ('Other', 'Other'),
]


class BookingForm(forms.ModelForm):
    """
    Creating a custom form to handle bookings
    """
    project_type = forms.ChoiceField(choices=PROJECTTYPE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    project_details = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    
    date = forms.DateField(
        widget=DatePickerInput(
            options={
                "format": "YYYY-MM-DD",
                "minDate": (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d'),
                "maxDate": (datetime.now() + timedelta(days=365)).strftime('%Y-%m-%d'),
                "showTodayButton": True,
            },
            attrs={"class": "form-control"},
        ),
        help_text="Choose a date: 'YYYY-MM-DD'",
    )

    time = forms.ChoiceField(
        choices=[
            ('09:00', '09:00 - 10:00'),
            ('10:00', '10:00 - 11:00'),
            ('11:00', '11:00 - 12:00'),
            ('13:00', '13:00 - 14:00'),
            ('14:00', '14:00 - 15:00'),
            ('17:00', '17:00 - 18:00'),
            ('18:00', '18:00 - 19:00'),
        ],
        widget=forms.Select(attrs={'class': 'form-control'}),
        help_text="Choose a time from available options",
    )

    class Meta:
        model = Booking
        fields = [
            'first_name',
            'last_name',
            'email',
            'date',
            'time',
            'project_type',
            'project_details'
            ]

    def clean(self):
    # Checking if the user already has a booking at the chosen date and prevents doublebookings 
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        if date:
            existing_booking = Booking.objects.filter(date=date).exists()
            if existing_booking:
                raise forms.ValidationError("You already have booked a session for this date.")
        return cleaned_data