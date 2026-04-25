
import re
from django.db import connection

def regex_func(pattern, string):
    return bool(re.match(pattern, string))

# Register the function
def create_regex_function():
    connection.create_function("REGEXP", 2, regex_func)
