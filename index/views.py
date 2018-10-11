from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
# Create your views here.

from weather_service.models import CityWeather
from weather_service.apps import WeatherServiceConfig

services = [
	WeatherServiceConfig,
	]
class Index(View):
	def get(self, request):
		widgets = []
		print(services)
		for service in services:
			print(service)
			for widget in service.widgets:
				for w in widget["model"].objects.filter(user=request.user):
					widgets.append({
						"template": "widgets/" + widget["name"] + ".html",
						"template_name": widget["name"],
						"data": w.get(),
					})
		return render(request, 'index.html', {
			'widgets': widgets,
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
						f = form.save(commit=False)
						f.user = request.user
						f.save()
						return redirect('home')
		return redirect('addWidget')