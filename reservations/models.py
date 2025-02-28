from django.db import models
from flights.models import Flight
from django.core.mail import send_mail
import random
import string
from django.conf import settings

class Reservation(models.Model):
    passenger_name = models.CharField(max_length=100)
    passenger_email = models.EmailField()
    reservation_code = models.CharField(max_length=10, unique=True, blank=True)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name="reservations")
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
     
        if not self.reservation_code:
            self.reservation_code = self.generate_reservation_code()

      
        if self.is_full():
            raise ValueError("This flight is fully booked. No more reservations can be made.")

        
        super().save(*args, **kwargs)
        self.send_confirmation_email()

    def generate_reservation_code(self):
   
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))  

    def is_full(self):
       
        return self.flight.reservations.count() >= self.flight.airplane.capacity

    def send_confirmation_email(self):
       
        subject = f"Reservation Confirmation for {self.passenger_name}"
        message = f"Dear {self.passenger_name},\n\nYour reservation for flight {self.flight.flight_number} is confirmed.\n\nThank you for choosing us!"

        send_mail(
            subject, 
            message, 
            settings.DEFAULT_FROM_EMAIL, 
            [self.passenger_email],  
            fail_silently=False,
        )

    def __str__(self):
        return f"Reservation for {self.passenger_name} on flight {self.flight.flight_number}"
