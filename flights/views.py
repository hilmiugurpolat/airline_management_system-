from rest_framework import generics
from .models import Flight
from .serializers import FlightSerializer  
from reservations.serializers import ReservationSerializer  
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class FlightList(generics.ListCreateAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['departure', 'destination', 'departure_time', 'arrival_time']
    ordering_fields = ['departure_time', 'arrival_time']
    ordering = ['departure_time']

    def perform_create(self, serializer):
      
        serializer.save()


class FlightDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


class FlightReservations(generics.ListAPIView):
    serializer_class = ReservationSerializer  

    def get_queryset(self):
      
        flight_id = self.kwargs['flight_id']  
        flight = Flight.objects.get(id=flight_id) 
        return flight.reservations.all()  