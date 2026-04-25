
from django.db import models, connection
from django.db.models import Func

class Regexp(Func):
    function = 'REGEXP'

    def __init__(self, expression, *args, **kwargs):
        super().__init__(expression, *args, **kwargs)

# Register the function
def add_regex_support():
    with connection.cursor() as cursor:
        cursor.execute("CREATE FUNCTION REGEXP(pattern, value) RETURNS INTEGER AS $$ "
                       "SELECT 1 WHERE value ~ pattern; $$ LANGUAGE SQL;")

# Call this function at the start of your application
add_regex_support()
