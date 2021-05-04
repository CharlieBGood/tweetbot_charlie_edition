import os
import tweepy 
from django.db.models.signals import post_save
from django.dispatch import receiver
from .credentials import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

from .models import Post

@receiver(post_save, sender=Post)
def tweet_post(sender, instance, **kwargs):
    twitter_auth_keys = {
        "CONSUMER_KEY": os.environ.get("CONSUMER_KEY"),
        "CONSUMER_SECRET": os.environ.get("CONSUMER_SECRET"),
        "ACCESS_TOKEN": os.environ.get("ACCESS_TOKEN"),
        "ACCESS_TOKEN_SECRET": os.environ.get("ACCESS_TOKEN_SECRET")
    }

    auth = tweepy.OAuthHandler(
        twitter_auth_keys['CONSUMER_KEY'],
        twitter_auth_keys['CONSUMER_SECRET']
    )
    auth.set_access_token(
        twitter_auth_keys['ACCESS_TOKEN'],
        twitter_auth_keys['ACCESS_TOKEN_SECRET']
    )
    api = tweepy.API(auth)

    if instance.tweet_type == 'joke' or instance.tweet_type == 'chuck_fact':
        tweet =  instance.content + '\n#TweetBotCharlieEdition'

    elif instance.tweet_type == 'quote':
        tweet = instance.content + '\n\n' + instance.author + '\n#TweetBotCharlieEdition' 

    elif instance.tweet_type == 'movie_review':
        tweet = instance.title + '\n' + instance.content + '\n' + instance.link + '\n' + instance.author

    try:
        api.update_status(tweet)
    except tweepy.TweepError as error:

        if error.api_code == 187:
            print('duplicate message')