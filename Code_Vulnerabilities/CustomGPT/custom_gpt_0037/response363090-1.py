
import re
from django.db import connection

def regex_match(pattern, string):
    if string is None:
        return False
    return bool(re.match(pattern, string))

def create_regex_function():
    connection.create_function("REGEXP", 2, regex_match)

# Call this in your app's startup code (e.g., in ready method of your AppConfig)
create_regex_function()
