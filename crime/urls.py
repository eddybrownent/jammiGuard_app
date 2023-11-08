from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('crime_details/<uuid:incident_id>/', views.crime_details, name='crime_details'),
    path('add_crime_incident/', views.add_crime_incident, name='add_crime_incident'),
    path('select_location/', views.select_location, name='select_location'),
]
