from django.db import models

# Create your models here.
# flywithme/models.py
from django.db import models


class Flight(models.Model):
    FlightId = models.AutoField(primary_key=True)
    DepAirport = models.CharField(max_length=50)
    DepDate = models.DateField()
    DepTime = models.TimeField()
    ArrAirport = models.CharField(max_length=50)
    ArrDate = models.DateField()
    ArrTime = models.TimeField()

    def __str__(self):
        return f"{self.FlightId}: {self.DepAirport} to {self.ArrAirport}"