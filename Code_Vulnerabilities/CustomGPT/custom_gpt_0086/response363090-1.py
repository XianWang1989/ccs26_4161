
import re
from django.db import connection

def regex_search(value, pattern):
    return bool(re.match(pattern, value))

# Register the function with SQLite
def create_regex_function():
    connection.cursor().execute('CREATE FUNCTION regex_search(value TEXT, pattern TEXT) RETURNS INTEGER AS $$ SELECT CASE WHEN $1 ~ $2 THEN 1 ELSE 0 END; $$ LANGUAGE SQL;')

create_regex_function()
