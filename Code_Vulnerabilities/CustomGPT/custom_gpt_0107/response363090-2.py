
import sqlite3
from django.db import connection

def regex_func(pattern, string):
    import re
    return re.search(pattern, string) is not None

def activate_regex():
    db = connection.cursor().connection
    db.create_function("REGEXP", 2, regex_func)

# Call this function in your Django app’s startup
activate_regex()
