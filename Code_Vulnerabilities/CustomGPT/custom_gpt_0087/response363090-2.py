
import re
from django.db import connection

def regex_func(expr, pattern):
    return 1 if re.search(pattern, expr) else 0

def connect_database():
    connection = sqlite3.connect('your_database.db')
    connection.create_function("REGEXP", 2, regex_func)
    return connection
