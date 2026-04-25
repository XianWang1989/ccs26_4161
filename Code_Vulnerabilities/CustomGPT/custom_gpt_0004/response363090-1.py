
import re
from django.db import connection

def regex_search(value, pattern):
    return re.match(pattern, value) is not None

# Register the custom function when the app is ready
def register_regex_function():
    with connection.cursor() as cursor:
        cursor.execute("CREATE FUNCTION regexp(pattern TEXT, value TEXT) RETURNS INTEGER AS $$
            BEGIN
                RETURN CASE WHEN value IS NOT NULL AND value ~ pattern THEN 1 ELSE 0 END;
            END $$ LANGUAGE plpgsql;")

# Call this function in your AppConfig's ready method
class MyAppConfig(AppConfig):
    name = 'myapp'

    def ready(self):
        register_regex_function()
