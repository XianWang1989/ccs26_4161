
import re
from django.db import connection

def regex_search(value, pattern):
    if value is None:
        return False
    return bool(re.match(pattern, value))

def activate_regex():
    connection.Connection.create_function('REGEXP', 2, regex_search)
