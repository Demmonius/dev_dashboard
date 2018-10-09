from django.apps import AppConfig


class WeatherServiceConfig(AppConfig):
	name = 'weather'

	about = {
        	"name": name,
        	"widgets": [{
			"name": "city_weather" ,
        	    	"description": "Show the city's weather" ,
        	    	"params": [{
				"name": "city" ,
				"type": "string"
			}]
		}]
	}

	args = [x["params"] for x in about["widgets"]]
	api_route = "city_weather"