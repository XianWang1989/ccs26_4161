
import sqlite3
import re
from django.db import connection

# Define a custom regex function
def regex_function(pattern, string):
    return re.match(pattern, string) is not None

# Register the function with SQLite
with connection.cursor() as cursor:
    cursor.execute("CREATE FUNCTION regexp(pattern TEXT, string TEXT) RETURNS BOOLEAN AS 'SELECT regexp(?1, ?2)'", (regex_function,))

# Then use it in your query
REGEX_ENTRANCE = r'^{0},|,{0},|,{0}$|^{0}$'.format(REQUEST_TYPE_ENTRANCE)
entrance_registers = EntranceRegister.objects.raw("""
    SELECT * FROM porter_entranceregister
    WHERE regexp(%s, authorized_requests)
""", [REGEX_ENTRANCE])
