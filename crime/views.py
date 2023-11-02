from django.shortcuts import render, redirect
from .models import Crimeincidents
from crime.forms import CrimeIncidentForm
from django.urls import reverse
from django.db.models import Count
import matplotlib.pyplot as plt
from django.db.models.functions import TruncDay 
from django.db.models import Count


def home(request):
    # Query the CrimeIncidents model to get all crime incidents
    crime_data = []
    plot_data = []
    location_crime_counts = Crimeincidents.objects.values('location').annotate(crime_count=Count('location')).order_by('-crime_count')
    
    if location_crime_counts:
        highest_crime_location = location_crime_counts[0]['location']
        highest_crime_count = location_crime_counts[0]['crime_count']
    else:
        highest_crime_location = "No data available"
        highest_crime_count = 0
    
        # Query the data and group by time intervals (e.g., months) and crime types
    plot_data = Crimeincidents.objects.annotate(
        time_interval=TruncDay('datetime')
    ).values('time_interval', 'crimetype').annotate(
        crime_count=Count('incidentid')
    ).order_by('time_interval')


    # Prepare data for the chart
    time_intervals = sorted(set(item['time_interval'] for item in plot_data))
    crime_types = sorted(set(item['crimetype'] for item in plot_data))

    data = {crime_type: [] for crime_type in crime_types}

    for item in plot_data:
        data[item['crimetype']].append(item['crime_count'])


    fig, ax = plt.subplots(figsize=(10, 6))

    for crime_type in crime_types:
        counts = [data[crime_type][i] if i < len(data[crime_type]) else 0 for i in range(len(time_intervals))]
        ax.fill_between(time_intervals, counts, label=crime_type)

    ax.set_xlabel('Time Interval')
    ax.set_ylabel('Crime Count')
    ax.set_title('Composition of Crimes by Type Over Time')
    ax.legend()

    plt.savefig("crime/static/crime/images/stacked_area_chart.png")
    
    latest_crimes = Crimeincidents.objects.order_by('datetime')[::-1][:3]
    crime_count = Crimeincidents.objects.count()
    for incident in Crimeincidents.objects.all():
        crime_data.append({
            'latitude': float(incident.latitude),
            'longitude': float(incident.longitude),
            'crime_type': incident.crimetype,
            'description': incident.description,
            'crime_details_url': reverse('crime_details', args=[str(incident.incidentid)]),
        })

    context = {
        'crime_count': crime_count,
        'crime_data': crime_data,
        'latest_crimes': latest_crimes,
        'highest_crime_location': highest_crime_location,
        'highest_crime_count': highest_crime_count,
        'plot_data': plot_data,
    }
    return render(request, 'crime/home.html', context)

# Your crime details view
def crime_details(request, incident_id):
    incident = Crimeincidents.objects.get(incidentid=incident_id)  # Use 'incidentid'

    context = {
        'crime_type': incident.crimetype,
        'description': incident.description,
        'datetime': incident.datetime,  # Add more fields as needed
    }

    return render(request, 'crime/crime_details.html', context)

def add_crime_incident(request):
    latitude = request.GET.get('latitude')
    longitude = request.GET.get('longitude')
    
    if request.method == 'POST':
        form = CrimeIncidentForm(request.POST)
        if form.is_valid():
            if latitude and longitude:
                form.instance.latitude = latitude
                form.instance.longitude = longitude
            form.save()
            return redirect('home')
    else:
        form = CrimeIncidentForm()
        if latitude and longitude:
            form.fields['latitude'].initial = latitude
            form.fields['longitude'].initial = longitude

    return render(request, 'crime/add_crime_incident.html', {'form': form, 'latitude': latitude, 'longitude': longitude})


def select_location(request):
    return render(request, 'crime/select_location.html')


def about(request):
    return render(request, 'crime/about.html', {'title': 'About'})

