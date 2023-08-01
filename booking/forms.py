from django import forms
from .models import Booking

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
    date_and_time = forms.DateTimeField(
        input_formats=["%Y-%m-%d %H:%M"],
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        help_text="Enter date and time in this format: 'YYYY-MM-DD HH:mm'"
    )

    class Meta:
        model = Booking
        fields = [
            'first_name',
            'last_name',
            'email',
            'date_and_time',
            'project_type',
            'project_details'
            ]