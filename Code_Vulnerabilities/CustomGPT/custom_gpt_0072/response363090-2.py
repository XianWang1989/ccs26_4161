
import re
from django.db import connection

def regex_function(value, pattern):
    return bool(re.match(pattern, value))

# Register the function with SQLite
def create_regex_function():
    connection.create_function("REGEXP", 2, regex_function)

# Call this function somewhere in your setup code
create_regex_function()
