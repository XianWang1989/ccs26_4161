
import re
from django.db import connection

def regex_search(value, pattern):
    return 1 if re.search(pattern, value) else 0

def create_regex_function():
    connection.create_function('REGEXP', 2, regex_search)

# Call this function before your query, for example in ready method of AppConfig
class YourAppConfig(AppConfig):
    name = 'your_app'

    def ready(self):
        create_regex_function()
