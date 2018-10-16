from django.apps import AppConfig

from .models import Youtube_subs, Youtube_views
from .form import Youtube_subsForm, Youtube_viewsForm

from api.views import YoutubeSubsViewSet, Youtube_viewsViewSet
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
		}, {
			"name": "Youtube_views",
        	    	"description": "Stats about a video",
        	    	"params": [{
				        "name": "video id",
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
	}, {
		"name": about["widgets"][1]["name"],
		"model": Youtube_views,
		"form": Youtube_viewsForm,
		"api": {
			"api_route": "youtube_views",
			"api_url": "/api/youtube_views",
			"ViewSet": YoutubeSubsViewSet,
			"Serializer": YoutubeSubsSerializer
		}
	}]