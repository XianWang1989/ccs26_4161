
import re
from django.db import connection

REQUEST_TYPE_ENTRANCE = 1
REGEX_ENTRANCE = r'^{0},|,{0},|,{0}$|^{0}$'.format(REQUEST_TYPE_ENTRANCE)

# Register the regex function
def register_regex_function():
    connection.create_function("regexp", 2, lambda pattern, value: 1 if re.search(pattern, value) else 0)

# Call this method in your application's startup
register_regex_function()

entrance_registers = EntranceRegister.objects.extra(
    where=["authorized_requests REGEXP %s"],
    params=[REGEX_ENTRANCE]
).order_by('-created_at')
