from rest_framework import serializers
from .models import Flight
from django.utils import timezone

from rest_framework import serializers
from .models import Flight

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ['id', 'flight_number', 'departure', 'destination', 'departure_time', 'arrival_time', 'airplane']

    def validate_departure_time(self, value):
      
        if value < timezone.now():
            raise serializers.ValidationError("Departure time must be in the future.")
        return value

    def validate(self, data):
      
        if data['departure_time'] >= data['arrival_time']:
            raise serializers.ValidationError("Arrival time must be after departure time.")
        return data

    def validate_flight_number(self, value):
       
        if Flight.objects.filter(flight_number=value).exists():
            raise serializers.ValidationError("This flight number already exists.")
        return value
