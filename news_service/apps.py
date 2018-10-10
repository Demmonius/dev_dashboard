from django.apps import AppConfig


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
			"api_route": "news",
		}]
	}
    
