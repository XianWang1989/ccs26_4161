
import re
from django.db import connection
from django.apps import AppConfig

class MyAppConfig(AppConfig):
    name = 'myapp'

    def ready(self):
        def regex_func(pattern, string):
            return re.search(pattern, string) is not None

        connection.create_function("REGEXP", 2, regex_func)
