
import re
from django.db import connection

def sqlite_regex_function():
    def regexp(pattern, string):
        if string is None:
            return False
        return bool(re.match(pattern, string))

    connection.create_function('REGEXP', 2, regexp)
