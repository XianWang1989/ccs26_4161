
from django.db import connection
import re

def add_regex_function():
    def regex(pattern, string):
        return re.match(pattern, string) is not None

    connection.create_function("REGEXP", 2, regex)

# Call this function after setting up your Django app
add_regex_function()
