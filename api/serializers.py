from rest_framework import serializers
from django.contrib.auth.models import User

from weather_service.models import CityWeather

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class CityWeatherSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = CityWeather
		fields = '__all__'