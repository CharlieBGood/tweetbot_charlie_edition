from django.db import models

# Create your models here.

class Post(models.Model):
	author = models.CharField(max_length=50, blank=True, null=True)
	content = models.TextField()
	link = models.TextField(blank=True, null=True)
	tweet_type = models.CharField(max_length=10, default='')
	title = models.CharField(max_length=100, blank=True, null=True)

	