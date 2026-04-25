
import re
from django.db import connection

def regex_match(value, pattern):
    return re.search(pattern, value) is not None

# Register the function at the start of your app
def activate_sqlite_regex():
    connection.connection.create_function("REGEXP", 2, regex_match)
