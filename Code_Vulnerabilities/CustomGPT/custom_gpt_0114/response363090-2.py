
import sqlite3
from django.db import connection

# Create the regular expression function
def regex_search(x, y):
    import re
    return re.search(y, x) is not None

# Register the function with SQLite
def register_regex_function():
    conn = connection.connection
    conn.create_function("REGEXP", 2, regex_search)

# Call this function before your query
register_regex_function()

# Now you can use REGEXP in your query
entrance_registers = EntranceRegister.objects.filter(authorized_requests__regex=REGEX_ENTRANCE)
