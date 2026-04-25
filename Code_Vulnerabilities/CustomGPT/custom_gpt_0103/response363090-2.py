
import sqlite3
import re
from django.db.backends.signals import connection_created

def create_regex_function(connection, **kwargs):
    def regex_match(pattern, string):
        return re.match(pattern, string) is not None

    connection.create_function("REGEXP", 2, regex_match)

# Connect and register
connection_created.connect(create_regex_function)
