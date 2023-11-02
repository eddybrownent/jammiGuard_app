from django.db import models
import uuid

# Create your models here.
class Crimeincidents(models.Model):
    incidentid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    crimetype = models.CharField(db_column='CrimeType', max_length=50) 
    datetime = models.DateTimeField(auto_now_add=True)  
    location = models.CharField(db_column='Location', max_length=255)  
    description = models.TextField(db_column='Description')
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.crimetype