from rest_framework import serializers
from .models import Reservation
import random
import string

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['id', 'passenger_name', 'passenger_email', 'reservation_code', 'flight', 'status', 'created_at']

    def validate_passenger_email(self, value):
        """Validate that email is in correct format."""
        if '@' not in value:
            raise serializers.ValidationError("Invalid email address.")
        return value

    def validate(self, data):
        """Ensure flight has available seats."""
        flight = data.get('flight')
        
        # flight.reservation_set.count() yerine, ters ilişkiyi doğruluyoruz
        total_reservations = Reservation.objects.filter(flight=flight).count()
        
        # Burada flight.airplane.capacity kullanıyoruz çünkü capacity Airplane modelinde tanımlı
        if flight.airplane.capacity <= total_reservations:
            raise serializers.ValidationError("Flight is fully booked.")
        
        return data



    def create(self, validated_data):
        """Generate a reservation code if not already provided and ensure it's unique."""
        if not validated_data.get('reservation_code'):
            while True:
                reservation_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
                if not Reservation.objects.filter(reservation_code=reservation_code).exists():
                    break
            validated_data['reservation_code'] = reservation_code
        
        # Create the reservation
        reservation = super().create(validated_data)
        
        # Send confirmation email to the passenger
        reservation.send_confirmation_email()
        
        return reservation
