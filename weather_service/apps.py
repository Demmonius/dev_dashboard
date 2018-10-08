from django.apps import AppConfig


class WeatherServiceConfig(AppConfig):
	name = 'weather'

	about = {
        	"name": name,
        	"widgets": [{
			"name": "city_temperature" ,
        	    	"description": "Show the city's temperature" ,
        	    	"params": [{
				"name": "city" ,
				"type": "string"
			}]
		}, {
			"name": "city_weather" ,
        	    	"description": "Show the city's weather" ,
        	    	"params": [{
				"name": "city" ,
				"type": "string"
			}]
		}]
	}
