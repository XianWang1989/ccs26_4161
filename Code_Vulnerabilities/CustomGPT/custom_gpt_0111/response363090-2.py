
import sqlite3
from django.db import connection

# Custom function to enable regex
def regex_function(conn, pattern, string):
    import re
    return re.match(pattern, string) is not None

# Register the custom function during the setup
def register_regex_function():
    with connection.cursor() as cursor:
        cursor.connection.create_function("REGEXP", 2, regex_function)

# Call this function somewhere in your setup
register_regex_function()

# Now you can use it in your queries
entrance_registers = EntranceRegister.objects.raw(
    'SELECT * FROM porter_entranceregister WHERE authorized_requests REGEXP ?',
    [REGEX_ENTRANCE]
)
