
import re
from django.db import connection

def regex_func(value, pattern):
    return re.search(pattern, value) is not None

# Register the function on startup
def register_regex_function():
    connection.create_function("regexp", 2, regex_func)

# Call this function at startup, perhaps in your AppConfig ready method
