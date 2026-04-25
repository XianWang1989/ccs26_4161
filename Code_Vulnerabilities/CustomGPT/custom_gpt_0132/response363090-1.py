
import re
from django.db import connection

def regex_search(pattern, value):
    return re.search(pattern, value) is not None

def add_regex_function():
    connection.create_function("REGEXP", 2, regex_search)

# Call this function in your app config or at the startup of your application.
add_regex_function()
