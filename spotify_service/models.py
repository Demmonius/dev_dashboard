from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class SpotifyPlayer(models.Model):
	title =  models.CharField(max_length=30)
	url = models.CharField(max_length=300)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def get(self, instance):
		return {
			'id': self.url.split('/')[-1]
		}

	def __str__(self):
		return "SpotifyPlayer " + self.title
	class Meta:
		verbose_name_plural = "Spotify players"