# Generated by Django 3.2.20 on 2023-10-23 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crime', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='crimeincidents',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='crimeincidents',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
