from django.urls import path
from .views import AirplaneList, AirplaneDetail, AirplaneFlights

urlpatterns = [
    path('', AirplaneList.as_view(), name='airplane-list'),  # Tüm uçakları listeleme ve ekleme
    path('<int:pk>/', AirplaneDetail.as_view(), name='airplane-detail'),  # Belirli bir uçağın detayları
    path('<int:pk>/flights/', AirplaneFlights.as_view(), name='airplane-flights'),  # Belirli bir uçağa ait uçuşlar
]
