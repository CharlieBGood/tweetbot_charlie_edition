"""tweetBot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from queries.views import home, tweet_random, tweet_quote, tweet_joke, tweet_chuck_fact, tweet_movie_review

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('tweet_random/', tweet_random),
    path('tweet_quote/', tweet_quote),
    path('tweet_joke/', tweet_joke),
    path('tweet_chuck_fact/', tweet_chuck_fact),
    path('tweet_movie_review/', tweet_movie_review)
]
