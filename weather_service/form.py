from django.forms import ModelForm, TextInput

from .models import CityWeather

class CityWeatherForm(ModelForm):
	class Meta:
		model = CityWeather
		fields = '__all__'
		widgets = {
			'city': TextInput(attrs={'class': ' form-control'}),
        	}