
import re
from django.db import connection

def regex_expression(field, pattern):
    return re.search(pattern, field) is not None

# Register the regex function
def create_connection():
    connection.connection.create_function("REGEXP", 2, regex_expression)

# Example usage in your query
create_connection()

REGEX_ENTRANCE = r'^{0},|,{0},|,{0}$|^{0}$'.format(REQUEST_TYPE_ENTRANCE)

entrance_registers = EntranceRegister.objects.raw(
    f"SELECT * FROM porter_entranceregister WHERE authorized_requests REGEXP ?",
    [REGEX_ENTRANCE]
)
