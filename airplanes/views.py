from rest_framework import generics
from .models import Airplane
from .serializers import AirplaneSerializer
from flights.models import Flight
from flights.serializers import FlightSerializer
from rest_framework import status
from rest_framework.response import Response

# Tüm uçakları listeleme ve yeni bir uçak ekleme
class AirplaneList(generics.ListCreateAPIView):
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer

# Belirli bir uçağın detaylarını alma, güncelleme ve silme
class AirplaneDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer

# Belirli bir uçağa ait uçuşları listeleme
class AirplaneFlights(generics.ListAPIView):
    serializer_class = FlightSerializer

    def get_queryset(self):
        airplane_id = self.kwargs['pk']
        return Flight.objects.filter(airplane_id=airplane_id)
