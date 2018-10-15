from django.db import models
from django.contrib.auth.models import User

from lxml import etree

import requests
# Create your models here.


class Gorafi(models.Model):
	xd = 0
	def get(self, instance):
		url = "http://www.legorafi.fr/feed/"
		gorafi_data = requests.get(url)
		
		tree = etree.parse(gorafi_data)
		tree["rss"]["channel"]["item"]