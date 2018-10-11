from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User

from news_service.models import News
from weather_service.models import CityWeather
from .serializers import CityWeatherSerializer, UserSerializer, NewsSerializer

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class CityWeatherViewSet(viewsets.ModelViewSet):
	queryset = CityWeather.objects.all()
	serializer_class = CityWeatherSerializer

class NewsViewSet(viewsets.ModelViewSet):
	queryset = News.objects.all()
	serializer_class = NewsSerializer