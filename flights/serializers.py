from rest_framework import serializers
from .models import Flight
from django.utils import timezone 

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ['id', 'flight_number', 'departure', 'destination', 'departure_time', 'arrival_time', 'airplane']

    def validate_departure_time(self, value):
        """Ensure departure time is in the future."""
        if value <  timezone.now():
            raise serializers.ValidationError("Departure time must be in the future.")
        return value

    def validate(self, data):
        """Ensure arrival time is after departure time."""
        if data['departure_time'] >= data['arrival_time']:
            raise serializers.ValidationError("Arrival time must be after departure time.")
        return data
