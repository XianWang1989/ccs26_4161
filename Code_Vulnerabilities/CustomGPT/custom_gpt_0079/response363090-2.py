
from django.db import connection

def regex_search(value: str, pattern: str):
    cursor = connection.cursor()
    cursor.execute(f"CREATE TEMP FUNCTION regex(pattern, value) RETURNS {pattern} AS 'path_to_your_function'")
    return cursor
