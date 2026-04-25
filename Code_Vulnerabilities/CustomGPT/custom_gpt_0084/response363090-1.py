
import re
from django.db import connection

def regex_match(value, pattern):
    return re.search(pattern, value) is not None

def create_regex_function():
    with connection.cursor() as cursor:
        cursor.execute("CREATE FUNCTION REGEXP(pattern TEXT, value TEXT) RETURNS INTEGER AS '$$' SELECT CASE WHEN $1 ~ $0 THEN 1 ELSE 0 END; $$ LANGUAGE SQL;")
