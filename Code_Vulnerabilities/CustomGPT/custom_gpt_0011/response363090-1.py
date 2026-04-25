
import re
from django.db import connection
from django.db.models import Func

# Custom regex function
class Regexp(Func):
    function = 'REGEXP'
    template = '%(expressions)s REGEXP %(string)s'

def create_regex_function():
    # Define a function to use with SQLite's standard connection
    def regexp(expr, string):
        return re.match(expr, string) is not None

    # Register the function with SQLite
    connection.create_function('REGEXP', 2, regexp)

# Call this function before querying
create_regex_function()

# Now you can use the Regexp function like this
REQUEST_TYPE_ENTRANCE = 1
REGEX_ENTRANCE = r'^{0},|,{0},|,{0}$|^{0}$'.format(REQUEST_TYPE_ENTRANCE)

entrance_registers = EntranceRegister.objects.filter(authorized_requests__regex=REGEX_ENTRANCE)
