from django import forms
from .models import Crimeincidents

class CrimeIncidentForm(forms.ModelForm):
    class Meta:
        model = Crimeincidents
        fields = ['crimetype', 'location', 'description', 'latitude', 'longitude']

    # Create choices for the "crimetype" field
    CRIME_TYPE_CHOICES = [
        ('Robbery', 'Robbery'),
        ('Assault', 'Assault'),
        ('Vandalism', 'Vandalism'),
        ('Violence', 'Violence'),
        ('Phone Theft', 'Phone Theft'),
        ('Other', 'Other'),

    ]
    
    crimetype = forms.ChoiceField(
        label="Crime Type",
        choices=CRIME_TYPE_CHOICES,
        help_text="Select the type of crime."
    )
    location = forms.CharField(label="Incident Location", help_text="E.g., Thika, City, or Town.")
        # Use Textarea widget for the "Description" field
    description = forms.CharField(
        label="Description",
        help_text="Describe In Few Words",
        widget=forms.Textarea(attrs={'rows': 2, 'cols': 20})
    )
    latitude = forms.DecimalField(label="Latitude", help_text="")
    longitude = forms.DecimalField(label="Longitude", help_text="")