
import re
from django.db import connection

def create_regex_function():
    def regex_func(pattern, string):
        return re.match(pattern, string) is not None

    connection.create_function("REGEXP", 2, regex_func)

# Call this function during startup
create_regex_function()
