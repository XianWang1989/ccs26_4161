
import re
from django.db import connection

def regexp(pattern, string):
    return re.match(pattern, string) is not None

# Register the function during app initialization
def register_custom_functions():
    connection.Connection.create_function("REGEXP", 2, regexp)

# Call the function in your app's ready() method
from django.apps import AppConfig

class YourAppConfig(AppConfig):
    name = 'your_app'

    def ready(self):
        register_custom_functions()
