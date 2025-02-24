from django.urls import path
from .views import ReservationList, ReservationDetail

urlpatterns = [
    path('', ReservationList.as_view(), name='reservation_list'),
    path('<int:pk>/', ReservationDetail.as_view(), name='reservation_detail'),
]
