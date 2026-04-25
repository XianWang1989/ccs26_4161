
import re
from django.db import connection

def regex_func(pattern, string):
    return re.match(pattern, string) is not None

def create_regex_function():
    connection.create_function("REGEXP", 2, regex_func)

