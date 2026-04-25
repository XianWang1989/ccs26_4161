
import re
from django.db import connection

def regex_search(value, pattern):
    return bool(re.search(pattern, value))

def create_regex_function():
    with connection.cursor() as cursor:
        cursor.execute("CREATE FUNCTION regexp(pattern, value) RETURNS INTEGER AS $$ "
                       "BEGIN "
                       "RETURN ($2 ~ $1); "
                       "END; $$ LANGUAGE plpgsql;")
