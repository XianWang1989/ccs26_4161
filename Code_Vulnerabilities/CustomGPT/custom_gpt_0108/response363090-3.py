
from django.apps import AppConfig

class YourAppConfig(AppConfig):
    name = 'yourapp'

    def ready(self):
        from . import create_regex_function
        create_regex_function()
