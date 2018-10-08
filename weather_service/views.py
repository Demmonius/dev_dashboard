from django.shortcuts import render
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist

from .models import CityWeather

import requests
# Create your views here.

def test(request):
	widget = CityWeather.objects.get(user=request.user)
	return render(request, 'weather.html', {'weather' : widget.getWeather()})