
import re
from django.db import connection

def regex_func(value, pattern):
    return bool(re.match(pattern, value))

# Register the function with SQLite
with connection.cursor() as cursor:
    cursor.execute("SELECT load_extension('regex')")

# Use it in your query
entrance_registers = EntranceRegister.objects.raw(
    'SELECT * FROM porter_entranceregister WHERE authorized_requests REGEXP %s',
    [REGEX_ENTRANCE]
)
