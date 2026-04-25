
import re
from django.db import connection

def regex_function(expr, pattern):
    return bool(re.match(pattern, expr))

def create_function():
    connection.connection.create_function("REGEXP", 2, regex_function)
