
import sqlite3
import re
from django.db import connection

def regex_func(expr, string):
    return re.search(expr, string) is not None

def add_regex_support():
    connection = sqlite3.connect(':memory:')  # Or your database path
    connection.create_function('REGEXP', 2, regex_func)
    connection.close()

# Call this function in your app's ready method
