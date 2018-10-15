from django.forms import ModelForm, TextInput

from .models import Youtube_subs

class Youtube_subsForm(ModelForm):
	class Meta:
		model = Youtube_subs
		exclude = ['user']
		widgets = {
			'channel': TextInput(attrs={'class': ' form-control'}),
        	}