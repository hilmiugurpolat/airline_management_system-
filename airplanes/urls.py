from django.urls import path
from .views import AirplaneList, AirplaneDetail, AirplaneFlights

urlpatterns = [
    path('', AirplaneList.as_view(), name='airplane-list'),  
    path('<int:pk>/', AirplaneDetail.as_view(), name='airplane-detail'),  
    path('<int:pk>/flights/', AirplaneFlights.as_view(), name='airplane-flights'),  
]
