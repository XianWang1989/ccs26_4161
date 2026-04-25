
import re
from django.db import connection

def sqlite_regex_func(expr, pattern):
    return re.search(pattern, expr) is not None

# Register the function
with connection.cursor() as cursor:
    cursor.execute("CREATE FUNCTION REGEXP(expr TEXT, pattern TEXT) RETURNS BOOLEAN AS 'sqlite_regex_func'")

# Then use it in your query
REGEX_ENTRANCE = r'^{0},|,{0},|,{0}$|^{0}$'.format(REQUEST_TYPE_ENTRANCE)

entrance_registers = EntranceRegister.objects.extra(where=[f"authorized_requests REGEXP '{REGEX_ENTRANCE}'"])
