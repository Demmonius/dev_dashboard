from django.db import models
from django.contrib.auth.models import User

import requests

class News(models.Model):
	TOPIC_CHOICES = (
        ("lequipe", "l'Equipe"),
        ('ign', 'IGN'),
        ('les-echos', 'Les Echos'),
        ('liberation', 'Liberation'),
    )
	topics = models.CharField(
        max_length = 15,
        choices = TOPIC_CHOICES,
        default = 'IGN',
    )
	onglet_to_display = models.IntegerField()
	user = models.ForeignKey(User, on_delete = models.CASCADE)

	

	def get(self, instance):
		url = "https://newsapi.org/v2/top-headlines?sources={}&apiKey=12114335eeee4844ac4dd869fc9a7f66&pageSize={}"
		new_info = requests.get(url.format(self.topics, self.onglet_to_display)).json()
		tab = []
		for elem in new_info['articles']:
			tab.append({
			'name' : elem['source']['name'],
			'title' : elem['title'],
			'pic' : elem['urlToImage'],
			})

		return {
			"tab" : tab,
			"id": instance.id,
		}

	def __str__(self):
		return "It's a pac of " + str(self.onglet_to_display) + " news of : " + self.topics

	class Meta:
        	verbose_name_plural = 'News'
# Create your models here.
