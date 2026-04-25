import re
from django.db import connection

def regexp(pattern, string):
    return re.search(pattern, string) is not None

connection.connection.create_function("REGEXP", 2, regexp)
