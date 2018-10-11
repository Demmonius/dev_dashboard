from rest_framework import serializers
from django.contrib.auth.models import User

from news_service.models import News
from weather_service.models import CityWeather
from spotify_service.models import SpotifyPlayer

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class CityWeatherSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = CityWeather
		fields = '__all__'

class NewsSerializer(serializers.HyperlinkedModelSerializer):
		class Meta:
			model = News
			fields = '__all__'

class SpotifyPlayerSerializer(serializers.HyperlinkedModelSerializer):
		class Meta:
			model = SpotifyPlayer
			fields = '__all__'