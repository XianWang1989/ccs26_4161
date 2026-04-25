
import re
from django.db import connection

def regex_search(value, pattern):
    return 1 if re.match(pattern, value) else 0

def add_regex_support():
    connection.create_function("REGEXP", 2, regex_search)

# Call this function on app startup or in the ready() method of your AppConfig
add_regex_support()
