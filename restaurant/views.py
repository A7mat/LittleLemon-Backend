from django.shortcuts import render
from django.contrib.auth.models import User

# from rest_framework.views import APIView
# from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet

from .models import MenuItem, Booking
from .serializers import MenuItemSerializer, BookingSerializer, UserSerializer

# Create your views here.
# def index(request):
#     return render(request, 'index.html', {})
class UserViewSet(ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [permissions.IsAuthenticated]

class MenuItemView(ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
        
class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
