
import re
from django.db import connection

def regex_match(value, pattern):
    if value is None:
        return False
    return re.match(pattern, value) is not None

# Registering the function with SQLite
def register_regex_function():
    with connection.cursor() as cursor:
        cursor.execute("CREATE FUNCTION regex_match(value TEXT, pattern TEXT) RETURNS BOOLEAN AS $$ "
                       "SELECT CASE WHEN value ~ pattern THEN 1 ELSE 0 END $$ LANGUAGE SQL;")

# Call this function when your app is ready
register_regex_function()
