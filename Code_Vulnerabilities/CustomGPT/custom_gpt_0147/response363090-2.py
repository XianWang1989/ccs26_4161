
import re
from django.db import connection
from django.db.models import Func
from myapp.models import EntranceRegister

# Custom REGEXP function for SQLite
def regex_func(expr, item):
    return re.search(expr, item) is not None

# Registering the regex function
def create_regex_function():
    connection = sqlite3.connect('your_database_name.db')
    connection.create_function("REGEXP", 2, regex_func)

# Use the custom function in your queryset
def get_entrance_registers():
    create_regex_function()  # Register the custom regex function

    REQUEST_TYPE_ENTRANCE = 1
    REGEX_ENTRANCE = r'^{0},|,{0},|,{0}$|^{0}$'.format(REQUEST_TYPE_ENTRANCE)

    entrance_registers = EntranceRegister.objects.raw(
        'SELECT * FROM porter_entranceregister WHERE authorized_requests REGEXP ?',
        [REGEX_ENTRANCE]
    )

    return entrance_registers
