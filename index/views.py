from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required
# Create your views here.

from weather_service.models import CityWeather
from weather_service.apps import WeatherServiceConfig

class Index(View):
	def get(self, request):
		return render(request, 'index.html', {
			'widgets': {
				'weather': [ x.getWeather() for x in CityWeather.objects.filter(user=request.user)]
			}
		})
	def post(self, request):
		pass

class AddWidget(View):
	def get(self, request):
		widgets = []
		for widget in [WeatherServiceConfig]:
			o = {
				'api_url': "/api/" + widget.api_route,
				'name': widget.name
			}
		widgets.append(o)
		return render(request, 'addWidget.html', {
			'widgets': widgets
		})
	
	def post(self, request):
		pass