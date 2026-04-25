
import re
from django.db import connection

def regex_function(expr, string):
    return re.search(expr, string) is not None

def connect_and_add_regex_function():
    connection.create_function("REGEXP", 2, regex_function)

# Call this function in your app's ready method.
