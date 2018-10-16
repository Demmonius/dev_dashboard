from django.forms import ModelForm, TextInput

from .models import Youtube_subs, Youtube_views

class Youtube_subsForm(ModelForm):
	class Meta:
		model = Youtube_subs
		exclude = ['user']
		widgets = {
			'channel': TextInput(attrs={'class': ' form-control'}),
        	}

class Youtube_viewsForm(ModelForm):
	class Meta:
		model = Youtube_views
		exclude = ['user']
		widgets = {
			'channel': TextInput(attrs={'class': ' form-control'}),
        	}