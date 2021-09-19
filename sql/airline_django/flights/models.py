from django.db import models

# Create your models here.



class Airport(models.Model):
    code = models.CharField(max_length=3, primary_key=True)
    name = models.CharField(max_length=64 )


class Flight (models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='departure')
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arrival')
    duratiion = models.IntegerField()


class Passenger (models.Model):
    flights = models.ManyToManyField(Flight, blank=True, related_name='passengers')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
