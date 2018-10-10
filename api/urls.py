from django.contrib import admin
from rest_framework import routers
from api.views import CityWeatherViewSet, UserViewSet
from django.urls import path, include

from weather_service.apps import WeatherServiceConfig

router = routers.DefaultRouter()

for service in [WeatherServiceConfig]:
	for widget in service.widgets:
        	router.register(widget["api"]["api_route"], widget["api"]["ViewSet"])
router.register('users', UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]