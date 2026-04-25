
import re
from django.db import connection

def regex_function(value, pattern):
    return bool(re.match(pattern, value))

def create_regex_function():
    connection.create_function("REGEXP", 2, regex_function)

# Call this function after your database connection is established
create_regex_function()
