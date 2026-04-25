
import re
from django.db import connection

def regex_search(value, pattern):
    return re.match(pattern, value) is not None

# Register the function with SQLite
def create_regex_function():
    connection = sqlite3.connect(':memory:')  # or your database
    connection.create_function("REGEXP", 2, regex_search)
    connection.close()

# Call this function at the start of your app
create_regex_function()
