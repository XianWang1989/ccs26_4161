
from application import manager

PLUGIN_NAME = "Example Plugin"

def plugin_function(options):
    # Do something
    print(f"{PLUGIN_NAME} function executed.")

# Register the plugin when it is imported
manager.register_plugin(PLUGIN_NAME, plugin_function)
