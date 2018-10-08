import time
import json

from django.views import View
from django.http import HttpResponse, JsonResponse

from weather_service.apps import WeatherServiceConfig

class About(View):
	def get(self, request):
		return JsonResponse({
			"client": {
				"host": self.get_client_ip(request)
			},
			"server": {
				"current_time": int(time.time()),
				"services": [x.about for x in [WeatherServiceConfig]]
			}
		})
	def get_client_ip(self, request):
		x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
		if x_forwarded_for:
			ip = x_forwarded_for.split(',')[0]
		else:
        		ip = request.META.get('REMOTE_ADDR')
		return ip