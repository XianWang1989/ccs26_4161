
import sqlite3
import re
from django.db import connection

def regex_match(expr, string):
    return re.match(expr, string) is not None

# Register the regex function
sqlite_conn = connection.connection  # Get SQLite connection
sqlite_conn.create_function("REGEXP", 2, regex_match)
