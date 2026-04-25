
import re
from django.db import connection

def regex_search(value, pattern):
    return bool(re.search(pattern, value))

# Register the function in SQLite
def create_regex_function():
    with connection.cursor() as cursor:
        cursor.execute("CREATE FUNCTION regexp(pattern TEXT, value TEXT) RETURNS BOOLEAN AS $$ SELECT CASE WHEN $2 ~ $1 THEN 1 ELSE 0 END $$ LANGUAGE SQL;")

create_regex_function()
