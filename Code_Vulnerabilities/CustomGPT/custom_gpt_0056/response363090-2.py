
import re
from django.db import connection

def create_regex_function():
    def regex_match(expr, string):
        return re.match(expr, string) is not None

    connection.create_function('REGEXP', 2, regex_match)

create_regex_function()
