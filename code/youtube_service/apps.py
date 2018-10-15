from django.apps import AppConfig

from .models import Youtube_subs
from .form import Youtube_subsForm

from api.views import YoutubeSubsViewSet
from api.serializers import YoutubeSubsSerializer

class YoutubeServiceConfig(AppConfig):
    name = 'Youtube_Service'

    about = {
        	"name": name,
        	"widgets": [{
			"name": "Youtube_subs" ,
        	    	"description": "Count subs of a channel" ,
        	    	"params": [{
				        "name": "channel_name",
				        "type": "string"
			}],
		}]
	}

    widgets = [{
		"name": about["widgets"][0]["name"],
		"model": Youtube_subs,
		"form": Youtube_subsForm,
		"api": {
			"api_route": "youtube_subs",
			"api_url": "/api/youtube_subs",
			"ViewSet": YoutubeSubsViewSet,
			"Serializer": YoutubeSubsSerializer
		}
	}]