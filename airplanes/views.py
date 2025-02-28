from rest_framework import generics
from .models import Airplane
from .serializers import AirplaneSerializer
from flights.models import Flight
from flights.serializers import FlightSerializer
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class AirplaneList(generics.ListCreateAPIView):
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer


class AirplaneDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer


class AirplaneFlights(generics.ListAPIView):
    serializer_class = FlightSerializer

    def get_queryset(self):
        airplane_id = self.kwargs['pk']
        get_object_or_404(Airplane, id=airplane_id)
        return Flight.objects.filter(airplane_id=airplane_id)
