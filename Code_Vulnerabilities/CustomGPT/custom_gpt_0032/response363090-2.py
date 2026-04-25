
from django.db import connection
import re

def regex_func(value, pattern):
    return re.search(pattern, value) is not None

# Register the custom regex function
def create_regex_function():
    connection.create_function("REGEXP", 2, regex_func)

# Call this right after your database is connected
create_regex_function()
