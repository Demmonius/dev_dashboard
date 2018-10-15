from django.apps import AppConfig

from .form import NewsForm
from .models import News
from api.views import NewsViewSet
from api.serializers import NewsSerializer

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
		"form": NewsForm,
		"api": {
			"api_route": "news",
			"api_url": "/api/news",
			"ViewSet": NewsViewSet,
			"Serializer": NewsSerializer
		}
	}]
    
