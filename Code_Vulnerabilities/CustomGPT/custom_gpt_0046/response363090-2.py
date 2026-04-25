
import re
from django.db import connection

def regex_match(expr, pattern):
    return bool(re.match(pattern, expr))

if not 'regex' in connection.ops.autocommit_sql_functions:
    connection.create_function('regex', 2, regex_match)

# Now use it in your query
REGEX_ENTRANCE = r'^{0},|,{0},|,{0}$|^{0}$'.format(REQUEST_TYPE_ENTRANCE)
entrance_registers = EntranceRegister.objects.raw(
    'SELECT * FROM porter_entranceregister WHERE authorized_requests REGEXP ?', [REGEX_ENTRANCE]
)
