
import sqlite3
from django.db import connection

# Define a function to add regex support to SQLite
def regex_function(x, y):
    import re
    return bool(re.match(x, y))

# Setting up the connection
with connection.cursor() as cursor:
    cursor.connection.create_function("REGEXP", 2, regex_function)

# Now you can use it in a query
entrance_registers = EntranceRegister.objects.extra(where=["authorized_requests REGEXP ?", REGEX_ENTRANCE])
