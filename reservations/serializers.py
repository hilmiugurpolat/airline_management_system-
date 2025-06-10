from rest_framework import serializers
from .models import Reservation, Flight
import random
import string

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['id', 'passenger_name', 'passenger_email', 'reservation_code', 'flight', 'status', 'created_at']

    def validate_passenger_email(self, value):
        
        if '@' not in value:
            raise serializers.ValidationError("Invalid email address.")
        return value

    def validate(self, data):
        
        
        if 'flight' in data:
            flight = data.get('flight')
            if flight is None:
                raise serializers.ValidationError("Flight is required.")  

            
            try:
                flight_obj = Flight.objects.get(id=flight.id)
            except Flight.DoesNotExist:
                raise serializers.ValidationError("Invalid flight ID.")  

          
            total_reservations = Reservation.objects.filter(flight=flight_obj).count()

          
            if flight_obj.airplane.capacity <= total_reservations:
                raise serializers.ValidationError("Flight is fully booked.")
        
        return data

    def create(self, validated_data):
       
        if not validated_data.get('reservation_code'):
            while True:
                reservation_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
                if not Reservation.objects.filter(reservation_code=reservation_code).exists():
                    break
            validated_data['reservation_code'] = reservation_code

        
        reservation = super().create(validated_data)

        
        reservation.send_confirmation_email()

        return reservation
