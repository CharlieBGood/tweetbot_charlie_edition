from django.apps import AppConfig


class PostsConfig(AppConfig):
    
    name = 'posts'

    def ready(self):
    	import posts.post
    	import posts.signals
