
import re
from django.db import connection

def regex_function(value, pattern):
    return re.match(pattern, value) is not None

def create_regex_function():
    with connection.cursor() as cursor:
        cursor.execute("CREATE FUNCTION REGEXP(pattern TEXT, value TEXT) RETURNS INTEGER AS $$ " 
                       "SELECT CASE WHEN value ~ pattern THEN 1 ELSE 0 END; $$ LANGUAGE SQL;")
