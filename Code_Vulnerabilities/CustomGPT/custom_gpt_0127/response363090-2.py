
import re
from django.db import connection

def regex_match(value, pattern):
    if value is None:
        return False
    return bool(re.match(pattern, value))

# Register the custom function
def create_regex_function():
    with connection.cursor() as cursor:
        cursor.execute("CREATE FUNCTION regexp(pattern TEXT, value TEXT) RETURNS INTEGER AS $$(SELECT CASE WHEN value IS NOT NULL AND value ~ pattern THEN 1 ELSE 0 END)$$ LANGUAGE SQL;")

# Call this function in your app’s ready() method
class YourAppConfig(AppConfig):
    name = 'your_app'

    def ready(self):
        create_regex_function()

# Now you can use the regex function in your query
entrance_registers = EntranceRegister.objects.extra(where=["regexp(%s, authorized_requests)" % REGEX_ENTRANCE])
