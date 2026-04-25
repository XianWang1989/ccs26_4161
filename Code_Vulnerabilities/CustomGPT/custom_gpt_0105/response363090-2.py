
import re
from django.db import connection

def regex_match(value, pattern):
    return re.match(pattern, value) is not None

# Register the regex function with SQLite
with connection.cursor() as cursor:
    cursor.executescript('CREATE FUNCTION REGEXP(pattern TEXT, value TEXT) RETURNS INTEGER AS $$ SELECT CASE WHEN value ~ pattern THEN 1 ELSE 0 END; $$ LANGUAGE SQL;')

# Then you can use it in your query
entrance_registers = EntranceRegister.objects.raw(
    'SELECT * FROM porter_entranceregister WHERE REGEXP(authorized_requests, ?) = 1',
    [REGEX_ENTRANCE]
)
