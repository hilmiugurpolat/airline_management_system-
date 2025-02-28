from django.db import models
from airplanes.models import Airplane
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import timedelta

class Flight(models.Model):
    flight_number = models.CharField(max_length=20, unique=True)
    departure = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    airplane = models.ForeignKey(Airplane, on_delete=models.CASCADE, related_name="flights")

    def __str__(self):
        return f"{self.flight_number} from {self.departure} to {self.destination}"

    def clean(self):
        """ Uçuş verilerini doğrular """
     
        if self.arrival_time <= self.departure_time:
            raise ValidationError("Arrival time must be after departure time.")
        
       
        if self.departure_time < timezone.now():
            raise ValidationError("Departure time cannot be in the past.")


        time_difference = self.arrival_time - self.departure_time
        if time_difference < timedelta(hours=1):
            raise ValidationError("There must be at least a 1-hour gap between flights for the same airplane.")

    def is_conflicting(self):
      
        
        conflicting_flights = Flight.objects.filter(
            airplane=self.airplane,
            departure_time__lt=self.arrival_time + timedelta(hours=1),
            arrival_time__gt=self.departure_time - timedelta(hours=1)
        ).exclude(id=self.id) 
        return conflicting_flights.exists()

    @property
    def reservations(self):
        return self.reservations.all()  
