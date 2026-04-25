
import re
from django.db import connection
from django.db.models import Func, F, Value, CharField

# Custom function to register the regex function in SQLite
def add_regex_function():
    with connection:
        connection.create_function("REGEXP", 2, lambda pattern, string: bool(re.search(pattern, string)))

# Call this function in your app’s ready method
class YourAppConfig(AppConfig):
    name = 'your_app_name'

    def ready(self):
        add_regex_function()
