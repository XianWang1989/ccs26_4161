
import sqlite3
from django.db import connection

def regex_func(expression, pattern):
    return re.match(pattern, expression) is not None

# Register the custom regex function
with connection.cursor() as cursor:
    connection.create_function("REGEXP", 2, regex_func)

# Now you can use it in your query
entrance_registers = EntranceRegister.objects.extra(
    where=["authorized_requests REGEXP ?", REGEX_ENTRANCE]
)
