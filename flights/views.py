from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .models import Flight
from .serializers import FlightSerializer

# Uçuşları listelemek ve yeni uçuş eklemek için sınıf
class FlightList(generics.ListCreateAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]  # Filtreleme ve sıralama için
    filterset_fields = ['departure', 'destination', 'departure_time', 'arrival_time']  # Hangi alanlardan filtreleme yapılacağı
    ordering_fields = ['departure_time', 'arrival_time']  # Sıralama yapılacak alanlar
    ordering = ['departure_time']  # Varsayılan sıralama

# Tekil bir uçuşun detaylarını görüntülemek, güncellemek veya silmek için sınıf
class FlightDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
