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
        ('Fraud', 'Fraud'),
        ('Burglary', 'Burglary'),
        ('Phone_Theft', 'Phone_Theft'),
        ('Theft', 'Theft'),
        ('Gun_crime', 'Gun_crime'),
        ('Other', 'Other'),

    ]
    
    crimetype = forms.ChoiceField(
        label="Crime Type",
        choices=CRIME_TYPE_CHOICES,
        help_text="Select the type of crime."
    )
    location = forms.CharField(label="Incident Location", help_text="E.g., Thika, City, or Town.")
        # Use Textarea widget for the "Description" field
  #  description = forms.CharField(
  #     label="Description",
  #      help_text="Describe In Few Words",
 #   )
latitude = forms.DecimalField(label="Latitude", help_text="")
longitude = forms.DecimalField(label="Longitude", help_text="")