from django.db import models
from django.contrib.auth.models import User
import urllib
import json
# Create your models here.

class Youtube_subs(models.Model):
	channel = models.CharField(max_length=30)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def get(self, instance):
		key = 'AIzaSyCC_5hS2vAiALrdUs7pZVk9QY8MAjREKLA'
		data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=" + self.channel + "&key=" + key).read()
		if len(json.loads(data)["items"]) == 0:
			return {'error': "Can't find " + self.channel + "'s channel"}
		subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
		data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=snippet&forUsername=" + self.channel + "&key=" + key).read()
		pic = json.loads(data)["items"][0]["snippet"]["thumbnails"]["default"]
		return {
			'subs': subs,
			'channel': instance.channel,
			'pic': pic,
		}

	def __str__(self):
		return "Subs of " + self.channel
	class Meta:
		verbose_name_plural = 'Channels subs'