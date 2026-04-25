
import re
from django.db import connection

def regex_operator(value, pattern):
    return re.match(pattern, value) is not None

def add_regex_function():
    connection.create_function("REGEXP", 2, regex_operator)
