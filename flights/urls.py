from django.urls import path
from .views import FlightList, FlightDetail


urlpatterns = [
    path('', FlightList.as_view(), name='flight-list'),  # Tüm uçuşları listeleme ve ekleme
    path('<int:pk>/', FlightDetail.as_view(), name='flight-detail'),  # Tekil uçuş detayı, güncelleme ve silme
]

