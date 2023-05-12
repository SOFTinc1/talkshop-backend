from django.db import models
from django.contrib.auth.models import User

class Comment(models.Model):
	content = models.TextField()
	# user = models.ForeignKey(User, on_delete=models.CASCADE)
	business = models.ForeignKey('Business', on_delete=models.CASCADE, related_name='comments')

class Category(models.Model):
	name = models.CharField(max_length=255)
	ordinal = models.IntegerField()
	business = models.ManyToManyField('Business')
	slug = models.CharField(max_length=100, unique=True, blank=True, null=True)

class Business(models.Model):
	ALL = 'All Tags'
	ANIMALS = 'Animals'
	SPORTS = 'Sports'
	GISTS = 'Gists'
	ENTERTAINMENT = 'Entertainment'
	HEALTH = 'Health'

	TAGS = [
		(ALL, 'All Tag'),
		(ANIMALS, 'Animals'),
		(SPORTS, 'Sports'),
		(GISTS, 'Gists'),
		(ENTERTAINMENT, 'Entertainment'),
		(HEALTH, 'Health'),
	]

	title = models.CharField(max_length=255)
	slug = models.CharField(max_length=100, unique=True, blank=True, null=True)
	description = models.TextField()
	tag = models.CharField(max_length=100, choices=TAGS, default=ALL)
	street_address = models.CharField(max_length=255)
	city = models.CharField(max_length=255)
	region = models.CharField(max_length=50)
	postal_code = models.CharField(max_length=50)
	country = models.CharField(max_length=50)
	website = models.URLField(max_length=255)
	infosource = models.CharField(max_length=255)
	hours = models.CharField(max_length=255)

