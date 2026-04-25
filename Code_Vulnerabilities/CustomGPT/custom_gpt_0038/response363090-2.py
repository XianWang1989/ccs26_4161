
import re
from django.db import connection

def regex_like(expr, pattern):
    return bool(re.match(pattern, expr))

def load_custom_regex_function():
    connection.connection.create_function('REGEXP', 2, regex_like)

# Call this function once on app startup
load_custom_regex_function()
