
import re
from django.db import connection

def regex_search(value, pattern):
    return re.match(pattern, value) is not None

# Register the regex function during the database connection
def create_regex_function():
    with connection.cursor() as cursor:
        connection.create_function("REGEXP", 2, regex_search)

# Ensure you call this function when setting up your database connection
create_regex_function()

# Now update your query as follows
REGEX_ENTRANCE = r'^{0},|,{0},|,{0}$|^{0}$'.format(REQUEST_TYPE_ENTRANCE)
entrance_registers = EntranceRegister.objects.raw(
    'SELECT * FROM porter_entranceregister WHERE authorized_requests REGEXP %s', [REGEX_ENTRANCE]
)
