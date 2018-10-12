from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
# Create your views here.

from spotify_service.apps import SpotifyServiceConfig
from weather_service.apps import WeatherServiceConfig
from news_service.apps import NewsServiceConfig

services = [
	WeatherServiceConfig,
	SpotifyServiceConfig,
	NewsServiceConfig,
	]
	
class Index(View):
	def get(self, request):
		widgets = []
		for service in services:
			for widget in service.widgets:
				for w in widget["model"].objects.filter(user=request.user):
					widgets.append({
						"template": "widgets/" + widget["name"] + ".html",
						"template_name": widget["name"],
						"data": w.get(w),
					})
		for w in widgets:
			if w["template_name"] == 'news_service':
				print(w["data"]["id"])
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

class Settings(View):
	def get(self, request):
		forms = []
		for service in services:
			for widget in service.widgets:
				for w in widget["model"].objects.filter(user=request.user):
					forms.append({
						'name': widget["name"],
						'form': widget["form"](instance=w),
						'object': w
					})
		print(forms)
		return render(request, 'settings.html', {
			'forms': forms,
		})

	def post(self, request):
		if request.POST["widget_name"] is None:
			return redirect('settings')
		for widgets in services:
			for widget in widgets.widgets:
				if widget["name"] == request.POST["widget_name"]:
					obj = widget["model"].objects.get(pk=request.POST["id"])
					if request.POST.get('delete'):
						print("DELETED")
						obj.delete()
						return redirect('home')
					form = widget["form"](request.POST, instance=obj)
					if form.is_valid():
						f = form.save(commit=False)
						f.user = request.user
						f.save()
						return redirect('home')
		return redirect('settings')