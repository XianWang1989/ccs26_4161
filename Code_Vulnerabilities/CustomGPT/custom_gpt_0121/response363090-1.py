
import re
from django.db import connection

def regex_func(expr, item):
    return re.match(expr, item) is not None

# Register the function with SQLite
def register_regex_function():
    with connection.cursor() as cursor:
        cursor.execute("CREATE FUNCTION REGEXP(expr TEXT, item TEXT) RETURNS BOOLEAN AS 'SELECT CASE WHEN ? IS NULL OR ? IS NULL THEN NULL ELSE ? END' " 
                       "LANGUAGE SQL", (expr, item, regex_func))
