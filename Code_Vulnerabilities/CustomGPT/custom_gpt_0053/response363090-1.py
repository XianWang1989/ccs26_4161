
import re
from django.db import connection

def regex_search(value, pattern):
    return bool(re.search(pattern, value))

# Register the function with SQLite
def create_regex_function():
    with connection.cursor() as cursor:
        cursor.execute("CREATE FUNCTION regex(pattern TEXT, value TEXT) RETURNS INTEGER AS $$"
                       "SELECT CASE WHEN value ~ pattern THEN 1 ELSE 0 END $$ LANGUAGE SQL;")
