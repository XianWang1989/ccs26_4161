
import re
from django.db import connection
from django.db.models import Q
from django.db.models.expressions import RawSQL

# Create a custom regex function for SQLite
def create_regexp_function():
    cursor = connection.cursor()
    cursor.execute("CREATE FUNCTION regexp(pattern TEXT, value TEXT) RETURNS INTEGER AS $$"
                   "SELECT CASE WHEN value IS NULL THEN 0 "
                   "ELSE 1 - (REGEXP '^'||pattern||'$' IN value) END; $$ LANGUAGE SQL;")

# Call this function in your app initialization
create_regexp_function()

# Example usage in your query
REQUEST_TYPE_ENTRANCE = 1
REGEX_ENTRANCE = r'^{0},|,{0},|,{0}$|^{0}$'.format(REQUEST_TYPE_ENTRANCE)

entrance_registers = EntranceRegister.objects.filter(
    RawSQL("regexp(%s, authorized_requests)", (REGEX_ENTRANCE,))
)

# Now you can access entrance_registers
print(list(entrance_registers))
