
import re
from django.db import connection

def regex_matcher(expr, value):
    return bool(re.match(expr, value))

def create_regex_function():
    connection.create_function("REGEXP", 2, regex_matcher)

# Make sure to call this function after your Django settings are set up.
create_regex_function()
