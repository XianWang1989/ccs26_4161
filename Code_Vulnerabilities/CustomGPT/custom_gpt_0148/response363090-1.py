
import re
from django.db import connection

def regex_function(expr, value):
    return re.match(expr, value) is not None

# Register the regex function in your Django app's ready method
def register_regex():
    with connection.cursor() as cursor:
        cursor.execute('CREATE FUNCTION REGEXP(expr TEXT, value TEXT) RETURNS BOOLEAN AS $$ '
                       'SELECT CASE WHEN value ~ expr THEN 1 ELSE 0 END; $$ LANGUAGE SQL;')

# Call this function after your Django app initializes
