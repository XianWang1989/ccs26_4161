
import re
from django.db import connection

def regex_func(value, pattern):
    return 1 if re.search(pattern, value) else 0

def connect():
    connection.connection.create_function("REGEXP", 2, regex_func)

# Call this function during your app's initialization
connect()
