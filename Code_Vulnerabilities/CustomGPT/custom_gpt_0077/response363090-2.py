
import re
from django.db import connection

def regex_func(value, pattern):
    return bool(re.match(pattern, value))

# Register the function with SQLite
def create_regex_function():
    connection.connection.create_function("REGEXP", 2, regex_func)
