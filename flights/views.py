from .models import Flight, Booking
from rest_framework.generics import ListAPIView
from .serializers import FlightsListSerializer, BookingsListSerializer
from datetime import date
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response



class FlightsList(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightsListSerializer

    #To render HTML Frontend
    
    # renderer_classes = [TemplateHTMLRenderer]
    # template_name = 'flightslist.html'
    
    # def get(self, request):
    #     queryset = Flight.objects.all()
    #     return Response({'flightslist': queryset})




class BookingsList(ListAPIView):
    queryset = Booking.objects.filter(date__gt=date.today())
    serializer_class = BookingsListSerializer

    #To render HTML Frontend

    # renderer_classes = [TemplateHTMLRenderer]
    # template_name = 'bookingslist.html'
    
    # def get(self, request):
    #     queryset = Booking.objects.all()
    #     return Response({'bookingslist': queryset})
