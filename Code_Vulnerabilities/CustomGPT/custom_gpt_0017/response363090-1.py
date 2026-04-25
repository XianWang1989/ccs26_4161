
import re
from django.db import connection

def regex_search(value, pattern):
    return re.match(pattern, value) is not None

def create_regex_function():
    with connection.cursor() as cursor:
        cursor.execute("CREATE FUNCTION regexp(pattern TEXT, value TEXT) RETURNS INTEGER AS $$ "
                       "BEGIN RETURN CASE WHEN value ~ pattern THEN 1 ELSE 0 END; END; $$ LANGUAGE plpgsql;")

# Call this function once, e.g., in the ready method of your AppConfig
class MyAppConfig(AppConfig):
    name = 'myapp'

    def ready(self):
        create_regex_function()
