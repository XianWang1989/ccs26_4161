
import re
from django.db import connection

def regex_function(expr, string):
    return 1 if re.search(expr, string) else 0

def setup_custom_functions():
    connection.connection.create_function("regexp", 2, regex_function)

# Call this function after your Django app has started
setup_custom_functions()
