
import re
from django.db import connection

def regex_like(value):
    return lambda search_string: bool(re.search(value, search_string))

# Register the regex function
def create_regex_function():
    connection.ensure_connection()
    connection.cursor().execute("CREATE FUNCTION REGEXP(pattern, text) RETURNS INTEGER AS 'SELECT CASE WHEN text REGEXP pattern THEN 1 ELSE 0 END'")
