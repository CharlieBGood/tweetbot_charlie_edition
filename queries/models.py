from django.db import models
from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

PERIODICITY = ( 
	("seconds", "Seconds"),
	("minutes", "Minutes"), 
	("hours", "Hours"),
	("days", "Days")
)

class Quote(models.Model):

	author = models.CharField(max_length=50)
	content = models.TextField()

class Joke(models.Model):
	joke = models.TextField(default='')
	setUp = models.TextField(default='')
	delivery = models.TextField(default='')

class ChuckFact(models.Model):
	searchString = models.TextField(blank=True, null=True, max_length=20)

class NYTMovieReview(models.Model):
	title = models.TextField()
	summaryShort = models.TextField()
	author = models.CharField(max_length=50)
	urlLink = models.TextField(default='')

class Random(models.Model):
	quotes = models.BooleanField()
	jokes = models.BooleanField()
	chuckNorris = models.BooleanField()
	movieReview = models.BooleanField()
	tweetingTimes = models.IntegerField(validators=[MinValueValidator(1)])
	periodicityNumber = models.IntegerField(validators=[MinValueValidator(1)])
	periodicity = models.CharField(max_length=7, choices=PERIODICITY, default='seconds')

class PersonalisedJoke(models.Model):
	categoryAny = models.BooleanField(default=True)
	categoryCustom = models.BooleanField(default=False)
	categoryProgramming = models.BooleanField(default=False)
	categoryMisc = models.BooleanField(default=False)
	categoryDark = models.BooleanField(default=False)
	categoryPun = models.BooleanField(default=False)
	categorySpooky = models.BooleanField(default=False)
	categoryChristmas = models.BooleanField(default=False)
	flagNsfw = models.BooleanField(default=False)
	flagReligious = models.BooleanField(default=False)
	flagPolitical = models.BooleanField(default=False)
	flagRacist = models.BooleanField(default=False)
	flagSexist = models.BooleanField(default=False)
	flagExplicit = models.BooleanField(default=False)
	searchString = models.TextField(blank=True, null=True)