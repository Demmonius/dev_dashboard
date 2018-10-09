from django.apps import AppConfig


class WeatherServiceConfig(AppConfig):
	name = 'weather'

	about = {
        	"name": name,
        	"widgets": [{
			"name": "City Weather" ,
        	    	"description": "Show the city's weather" ,
        	    	"params": [{
				"name": "city" ,
				"type": "string"
			}],
			"api_route": "city_weather",
		}]
	}