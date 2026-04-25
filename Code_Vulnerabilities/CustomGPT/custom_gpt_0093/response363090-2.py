
import sqlite3
from django.db import connection

def create_regex_function():
    connection = sqlite3.connect(':memory:')
    connection.create_function("REGEXP", 2, lambda x, y: True if re.match(y, x) else False)
    connection.close()

# Call this function when initializing your application
create_regex_function()
