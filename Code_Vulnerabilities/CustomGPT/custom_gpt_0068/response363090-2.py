
import re
from django.db import connection

def regex_function(expression, string):
    return re.search(expression, string) is not None

def create_regex_function():
    with connection.cursor() as cursor:
        cursor.create_function("REGEXP", 2, regex_function)

# Call this function when setting up your app
create_regex_function()
