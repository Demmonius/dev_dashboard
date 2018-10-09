from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User

from weather_service.models import CityWeather
from .serializers import CityWeatherSerializer, UserSerializer

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class CityWeatherViewSet(viewsets.ModelViewSet):
	queryset = CityWeather.objects.all()
	serializer_class = CityWeatherSerializer