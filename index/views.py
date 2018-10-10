from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
# Create your views here.

from weather_service.models import CityWeather
from weather_service.apps import WeatherServiceConfig

services = [WeatherServiceConfig]
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
		forms = []
		for service in services:
			for widget in service.widgets:
				forms.append({
					'name': widget["name"],
					'form': widget["form"](initial={'user': request.user})
					})
		return render(request, 'addWidget.html', {
			# 'widgets': [x.widgets for x in services],
			'forms': forms
		})
	
	def post(self, request):
		if request.POST["widget_name"] is None:
			return redirect('addWidget')
		for widgets in services:
			for widget in widgets.widgets:
				if widget["name"] == request.POST["widget_name"]:
					form = widget["form"](request.POST)
					if form.is_valid():
						form.save(commit=False)
						form.user = request.user
						form.save()
						return redirect('home')
		return redirect('addWidget')