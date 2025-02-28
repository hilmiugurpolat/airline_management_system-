from django.urls import path
from .views import FlightList, FlightDetail, FlightReservations

urlpatterns = [
    path('', FlightList.as_view(), name='flight-list'),
    path('<int:pk>/', FlightDetail.as_view(), name='flight-detail'),
    path('<int:flight_id>/reservations/', FlightReservations.as_view(), name='flight-reservations'),  
]
