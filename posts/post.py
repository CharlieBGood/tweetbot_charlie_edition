from .models import Post

from django.dispatch import receiver
from queries.signals import new_quote, new_joke, new_chuck_fact, new_movie_review 

@receiver(new_quote)
def post_quote(sender, **kwargs):
	Post.objects.create(author=sender.author, content=sender.content, tweet_type='quote')

@receiver(new_joke)
def post_joke(sender, **kwargs):
	if sender.joke:
		Post.objects.create(content=sender.joke)
	else:
		joke = sender.setUp + '\n' + sender.delivery
		Post.objects.create(content=joke, tweet_type='joke')


@receiver(new_chuck_fact)
def post_cuck_fact(sender, **kwargs):
	Post.objects.create(content=sender.searchString, tweet_type='chuck_fact')

@receiver(new_movie_review)
def post_movie_review(sender, **kwargs):
	Post.objects.create(author=sender.author, content=sender.summaryShort, title=sender.author, 
		link=sender.urlLink, tweet_type='movie_review')