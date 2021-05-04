from django.shortcuts import render, redirect
from django.contrib import messages 
from .forms import RandomForm, PersonalisedJokesForm, ChuckNorrisWordQuery
from .bot import random_func, job, quote_query, personalised_joke_query, chuck_norris_fact_query, nyt_movie_review_query
from .models import Random, PersonalisedJoke
import time, threading


# Create your views here.

def home(request):
	if request.method=='GET':
		form = RandomForm()
		joke_form = PersonalisedJokesForm()
		chuck_form = ChuckNorrisWordQuery()
	else:
		pass

	return render(request, 'index.html', {'form':form, 'joke_form':joke_form, 'chuck_form':chuck_form})


def tweet_random(request):
	if request.method=='POST':
		form = RandomForm(request.POST)

		if form.is_valid():
			if form.cleaned_data['quotes']==form.cleaned_data['jokes']==\
			form.cleaned_data['chuckNorris']==form.cleaned_data['movieReview']==False:
				messages.warning(request, 'Make sure you have selected at least one category', extra_tags='quotes')

			else:
				random_object = Random(**form.cleaned_data)
				random_func(random_object)

		else:
			messages.warning(request, 'Ensure periodicity value and tweeting times are greater than or equal to 1', extra_tags='quotes')
			
		return redirect('/')

	else:
		return redirect('/')


def tweet_quote(request):
	if request.method == 'POST':
		job(arguments=quote_query())

		return redirect('/')
	else:
		return redirect('/')


def tweet_joke(request):
	if request.method == 'POST':
		joke = PersonalisedJokesForm(request.POST)
		if joke.is_valid():
			if joke.cleaned_data['categoryCustom']==True and \
			joke.cleaned_data['categoryProgramming']==joke.cleaned_data['categoryMisc']==\
			joke.cleaned_data['categoryDark']==joke.cleaned_data['categoryPun']==\
			joke.cleaned_data['categorySpooky']==joke.cleaned_data['categoryChristmas']==False:
				
				joke.cleaned_data['categoryAny'] = True
				joke.cleaned_data['categoryCustom'] = False

			personalised_joke = PersonalisedJoke(**joke.cleaned_data)

			joke = personalised_joke_query(personalised_joke)
			
			if not joke:
				messages.error(request, 'No joke found with this specifications, please try again', extra_tags='jokes')
				return redirect('/')
				
			job(arguments=joke)

	return redirect('/')	


def tweet_chuck_fact(request):
	if request.method=='POST':
		fact = ChuckNorrisWordQuery(request.POST)
		if fact.is_valid():
			fact = chuck_norris_fact_query(words = [fact.cleaned_data['searchString']])
			if fact:
				job(arguments=fact)
			else:
				messages.error(request, 'No amazing fact found with this keyword, please try again', extra_tags='chuck_fact')
		return redirect('/')

def tweet_movie_review(request):
	if request.method == 'POST':
		job(arguments=nyt_movie_review_query())

		return redirect('/')
	else:
		return redirect('/')

