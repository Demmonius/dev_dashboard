from django.db import models
from django.contrib.auth.models import User

import requests

class News(models.Model):
	topic = models.CharField(max_length = 30) 
	user = models.ForeignKey(User, on_delete = models.CASCADE)

	def getNews(self):
		self.api_key = "12114335eeee4844ac4dd869fc9a7f66"
		url = "https://newsapi.org/v2/top-headlines?sources={}&apiKey={}"
		new_info = requests.get(url.format(self.topic, self.api_key)).json()
		return {
			'name' : new_info['articles'][0]['source']['name'],
			'title' : new_info['articles'][0]['title'],
			'pic' : new_info['articles'][0]['urlToImage']
		}

	def __str__(self):
		return "It's a new of: " + self.topic

	class Meta:
        	verbose_name_plural = 'News'
# Create your models here.
