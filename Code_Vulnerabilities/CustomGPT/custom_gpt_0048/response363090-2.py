
import re
from django.db import connection

def regex_match(sqlite_cursor, regex, string):
    if string is None:
        return False
    return bool(re.match(regex, string))

# Register the function in your Django app
def create_regex_function():
    with connection.cursor() as cursor:
        cursor.create_function("REGEXP", 2, regex_match)
