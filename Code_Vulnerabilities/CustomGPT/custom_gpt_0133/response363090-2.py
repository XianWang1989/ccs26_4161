
import regex
from django.db import connection

def regex_func(pattern, string):
    return 1 if regex.match(pattern, string) else 0

# Register the regex function with SQLite
with connection.cursor() as cursor:
    cursor.execute("CREATE FUNCTION regex(pattern TEXT, string TEXT) RETURNS INTEGER AS 'SELECT regex.func(pattern, string)'")
