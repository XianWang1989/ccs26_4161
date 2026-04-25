
import sqlite3
from django.db import connection

def regex_function(expr1, expr2):
    import re
    return 1 if re.search(expr1, expr2) else 0

with connection.cursor() as cursor:
    # Register the regex function with SQLite
    cursor.execute("CREATE FUNCTION regexp(pattern TEXT, value TEXT) RETURNS INTEGER AS $$"
                   "SELECT CASE WHEN value REGEXP pattern THEN 1 ELSE 0 END; $$ LANGUAGE SQL;")
