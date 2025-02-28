from rest_framework import generics
from .models import Reservation
from .serializers import ReservationSerializer

class ReservationList(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def perform_create(self, serializer):
      
        serializer.save()

class ReservationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def perform_update(self, serializer):
    
        serializer.save()

    def perform_destroy(self, instance):
       
        instance.delete()
