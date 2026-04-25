
import re
from django.db import connection
from django.db.models import Q

# Define the function to register your regex pattern with SQLite
def regex_search(expressions, value):
    return re.search(expressions, value) is not None

# Register the regex function with SQLite
def register_regex_function():
    with connection.cursor() as cursor:
        cursor.execute("CREATE FUNCTION REGEXP(pattern TEXT, value TEXT) RETURNS INTEGER AS "
                       "BEGIN "
                       "RETURN CASE WHEN value REGEXP pattern THEN 1 ELSE 0 END; "
                       "END;")

    connection.connection.create_function("REGEXP", 2, regex_search)

# Call this function within your app setup or before running tests
register_regex_function()

# Now you can write your query using the custom REGEXP function
REQUEST_TYPE_ENTRANCE = 1
REGEX_ENTRANCE = r'^{0},|,{0},|,{0}$|^{0}$'.format(REQUEST_TYPE_ENTRANCE)

# Modify your queryset
entrance_registers = EntranceRegister.objects.filter(
    Q(authorized_requests__regex=REGEX_ENTRANCE)
)

# Alternatively, use the raw expression as SQLite needs direct SQL
entrance_registers = EntranceRegister.objects.raw(
    'SELECT * FROM porter_entranceregister WHERE authorized_requests REGEXP %s', 
    [REGEX_ENTRANCE]
)
