
import re
from django.db import connection

def regex_function(value, pattern):
    if value is None:
        return 0
    return int(bool(re.match(pattern, value)))

# Register the regex function with the SQLite connection
def connect():
    connection.connection.create_function("regexp", 2, regex_function)

# Call this function when your app starts
connect()
