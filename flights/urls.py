from django.urls import path
from .views import FlightsList, BookingsList

urlpatterns = [
    path('flightslist', FlightsList.as_view(), name='flights-list'),
    path('bookingslist', BookingsList.as_view(), name='bookings-list')
]