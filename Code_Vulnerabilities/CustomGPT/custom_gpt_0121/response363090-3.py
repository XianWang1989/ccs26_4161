
# In your AppConfig's ready method
from django.apps import AppConfig

class YourAppConfig(AppConfig):
    name = 'your_app_name'

    def ready(self):
        register_regex_function()
