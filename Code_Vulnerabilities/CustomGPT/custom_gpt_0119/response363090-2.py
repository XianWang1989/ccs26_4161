
import sqlite3
import re

def regex_function(expr, string):
    if expr is None or string is None:
        return 0
    return 1 if re.search(expr, string) else 0

# Register the function in your Django database connection
from django.db import connection

with connection.cursor() as cursor:
    connection.create_function("REGEXP", 2, regex_function)
