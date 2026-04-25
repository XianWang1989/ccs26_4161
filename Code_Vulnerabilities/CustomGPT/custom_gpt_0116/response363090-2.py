
import re
from django.db import connection

def regex_match(value, pattern):
    return re.match(pattern, value) is not None

# Register the function
def create_custom_functions():
    connection.connection.create_function('regexp', 2, regex_match)

# Call this function when your app starts
create_custom_functions()
