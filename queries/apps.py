from django.apps import AppConfig


class QueriesConfig(AppConfig):
    
    name = 'queries'

    def ready(self):
    	import queries.bot
