
import sqlite3
from django.db import connection

def regex(sqlite_regexp, string, pattern):
    import re
    return re.match(pattern, string) is not None

# Add the function to the connection
def add_regex_function():
    connection.cursor().execute('CREATE FUNCTION regexp(pattern TEXT, value TEXT) RETURNS INTEGER AS '
                                 'RETURN CASE WHEN value REGEXP pattern THEN 1 ELSE 0 END;')

# Call this function when the database connection is established
add_regex_function()
