
import re
from django.db import connection

def regex_function(regex, string):
    return re.match(regex, string) is not None

# Register the function with SQLite
def create_regex_function():
    with connection.cursor() as cursor:
        cursor.execute("CREATE FUNCTION REGEXP(regex TEXT, string TEXT) RETURNS INTEGER AS $$ "
                       "SELECT CASE WHEN string ~ regex THEN 1 ELSE 0 END; $$ LANGUAGE sql;")
