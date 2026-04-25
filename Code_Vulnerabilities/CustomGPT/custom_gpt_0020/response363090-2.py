
import re
from django.db import connection

def regex_function(value, pattern):
    return re.match(pattern, value) is not None

# Registering the function with SQLite
def create_regex_function():
    connection.connection.create_function('REGEXP', 2, regex_function)

# Call this function in your Django app startup
create_regex_function()
