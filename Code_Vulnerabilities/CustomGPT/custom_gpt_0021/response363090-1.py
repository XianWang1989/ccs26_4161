
import re
from django.apps import AppConfig
from django.db import connection

class YourAppNameConfig(AppConfig):
    name = 'your_app_name'

    def ready(self):
        def regex_func(pattern, string):
            return re.search(pattern, string) is not None

        connection.create_function("REGEXP", 2, regex_func)
