
import re
from django.db import connection

def regex_function(expr, item):
    return re.match(expr, item) is not None

# Register the regex function
connection.connection.create_function("REGEXP", 2, regex_function)

# Now you can use REGEXP in your queries
entrance_registers = EntranceRegister.objects.raw('SELECT * FROM porter_entranceregister WHERE authorized_requests REGEXP ?', [REGEX_ENTRANCE])
