
import re
from django.db import connection

def regex_function(expr, pattern):
    return re.match(pattern, expr) is not None

# Register the function with the SQLite database
with connection:
    connection.create_function("REGEXP", 2, regex_function)
