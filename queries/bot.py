import requests, schedule, time, random, threading

from .models import Quote, Joke, ChuckFact, NYTMovieReview, Random
from .signals import new_quote, new_joke, new_chuck_fact, new_movie_review 
from jokeapi import  Jokes
from apscheduler.schedulers.background import BackgroundScheduler


def quote_query():

	url = "https://zenquotes.io/api/random"

	response = requests.request("GET", url).json()[0]
	author = response['a']
	content = response['q']
	quote = Quote.objects.create(author=author, content=content)

	return quote


def joke_query(**kwargs):

	j = Jokes()
	joke = j.get_joke(lang='en')

	if joke["type"] == "single": 
		joke = Joke.objects.create(joke=joke['joke'])
	else:
		joke = Joke.objects.create(setUp=joke['setup'], delivery=joke['delivery'])

	return joke


def personalised_joke_query(personalised_joke):
	j = Jokes()
	categories = []
	blacklist = []
	if personalised_joke.categoryCustom:
		if personalised_joke.categoryProgramming:
			categories.append('programming')
		if personalised_joke.categoryMisc :
			categories.append('misc')
		if personalised_joke.categoryDark:
			categories.append('dark')
		if personalised_joke.categoryPun:
			categories.append('pun')
		if personalised_joke.categorySpooky:
			categories.append('spooky')
		if personalised_joke.categoryChristmas:
			categories.append('christmas')
	if personalised_joke.flagNsfw:
			blacklist.append('nsfw')
	if personalised_joke.flagReligious:
			blacklist.append('religious')
	if personalised_joke.flagPolitical:
			blacklist.append('political')	
	if personalised_joke.flagRacist:
			blacklist.append('racist')	
	if personalised_joke.flagSexist:
			blacklist.append('sexist')	
	if personalised_joke.flagExplicit:
			blacklist.append('explicit')
	
	joke = j.get_joke(category=categories, lang='en', blacklist=blacklist, search_string=personalised_joke.searchString)
	
	if joke['error'] == True:
		return None

	if joke["type"] == "single": 
		joke = Joke.objects.create(joke=joke['joke'])
	else:
		joke = Joke.objects.create(setUp=joke['setup'], delivery=joke['delivery'])

	return joke


def chuck_norris_fact_query(**kwargs):

	if not kwargs:
		words = ['football', 'girls', 'boys', 'strong', 'funny', 'joke', 'athlete', 'spit', 'sun', 'god', 'kiwi']
	else:
		words = kwargs['words']

	url = "https://matchilling-chuck-norris-jokes-v1.p.rapidapi.com/jokes/search"

	querystring = {"query":random.choice(words)}

	headers = {
    	'accept': "application/json",
    	'x-rapidapi-key': "c5fd731b6dmsh64c589cb20d72ccp170340jsn4b36f5bb61aa",
    	'x-rapidapi-host': "matchilling-chuck-norris-jokes-v1.p.rapidapi.com"
    }

	response = requests.request("GET", url, headers=headers, params=querystring)
	
	try:
		if response.json()['total'] == 0:
			fact = None

		else:
			fact_phrase = random.choice(response.json()['result'])['value']
			fact = ChuckFact.objects.create(searchString=fact_phrase)
		
	except:
		if response.json()['status'] == 400:
			fact = None

	return fact


def nyt_movie_review_query():
	
	url = "https://api.nytimes.com/svc/movies/v2/reviews/picks.json?api-key=lfffRGzRGbrHX0tmKPDH7Is4b9CueCFb"

	response = requests.request("GET", url)
	review = random.choice(response.json()['results'])
	movieReview = NYTMovieReview.objects.create(title=review['headline'], summaryShort=review['summary_short'], 
		author =review['byline'], urlLink=review['link']['url'])

	return movieReview


def job(**kwargs):

	if type(kwargs['arguments']) == Quote:
		new_quote.send(sender=kwargs['arguments'])
	elif type(kwargs['arguments']) == Joke:
		new_joke.send(sender=kwargs['arguments'])
	elif type(kwargs['arguments']) == ChuckFact:
		new_chuck_fact.send(sender=kwargs['arguments'])
	elif type(kwargs['arguments']) == NYTMovieReview:
		new_movie_review.send(sender=kwargs['arguments'])
	elif type(kwargs['arguments']) == list:
		job(arguments=random.choice(kwargs['arguments'])())
		global counter
		counter += 1
		return


def random_func(random_object):

	functionsList = []
	if random_object.quotes:
		functionsList.append(quote_query)
	if random_object.jokes:
		functionsList.append(joke_query)
	if random_object.chuckNorris:
		functionsList.append(chuck_norris_fact_query)
	if random_object.movieReview:
		functionsList.append(nyt_movie_review_query)

	periodicityNumber = random_object.periodicityNumber
	periodicity = random_object.periodicity
	tweetingTimes = random_object.tweetingTimes

	global counter 
	counter = 0
	flag = True

	scheduler = BackgroundScheduler()
	if periodicity == 'seconds':
		scheduler.add_job(job, 'interval', seconds=periodicityNumber, kwargs={'arguments':functionsList})
	elif periodicity == 'minutes':
		scheduler.add_job(job, 'interval', minutes=periodicityNumber, kwargs={'arguments': functionsList})
	elif periodicity == 'hours':
		scheduler.add_job(job, 'interval', hours=periodicityNumber, kwargs={'arguments': functionsList})
	elif periodicity == 'days':
		scheduler.add_job(job, 'interval', days=periodicityNumber, kwargs={'arguments': functionsList})

	scheduler.start()
	while flag:
		if counter >= tweetingTimes:
		    flag = False
		    scheduler.shutdown()


def run_manually():

	answer = ''
	while not answer:
		answer = input('What kind of tweets would you like to post?\nJokes [j]\nQuotes [q]\nChuck Norris Fact [f]'+
			'\nMovie Reviews [m]\nAnswer: ')

		if answer == 'q':
			job(arguments=quote_query())
		elif answer == 'j':
			job(arguments=joke_query())
		elif answer == 'f':
			job(arguments=chuck_norris_fact())
		elif answer == 'm':
			job(arguments=nyt_movie_review())
		else:
			answer = ''

	#while True:
	#	schedule.run_pending()
	#	time.sleep(1)