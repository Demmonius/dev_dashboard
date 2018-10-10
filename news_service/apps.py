from django.apps import AppConfig

from .models import News
from api.serializers import NewsSerializer
from api.views import NewsViewSet

class NewsServiceConfig(AppConfig):
	name = 'news_service'

	about = {
        	"name": name,
        	"widgets": [{
			"name": "News" ,
        	    	"description": "Show the news" ,
        	    	"params": [{
				"name": "topic" ,
				"type": "string"
			}],
		}]
	}

	widgets = [{
		"name": name,
		"model": News,
		#"form": CityWeatherForm,
		"api": {
			"api_route": "news",
			"api_url": "/api/news",
			"ViewSet": NewsViewSet,
			"Serializer": NewsSerializer
		}
	}]
    
