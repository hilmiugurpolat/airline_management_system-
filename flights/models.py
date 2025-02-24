from django.db import models
from airplanes.models import Airplane

class Flight(models.Model):
    flight_number = models.CharField(max_length=20, unique=True)
    departure = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    airplane = models.ForeignKey(Airplane, on_delete=models.CASCADE, related_name="flights")

    def __str__(self):
        return f"{self.flight_number} from {self.departure} to {self.destination}"

    def is_conflicting(self):
        conflicting_flights = Flight.objects.filter(
            airplane=self.airplane,
            departure_time__lt=self.arrival_time,
            arrival_time__gt=self.departure_time
        ).exclude(id=self.id)  # Exclude the current flight from the conflict check
        return conflicting_flights.exists()
