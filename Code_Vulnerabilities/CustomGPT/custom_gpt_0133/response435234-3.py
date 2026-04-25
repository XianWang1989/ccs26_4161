
from application import manager

PLUGIN_NAME = "Example Plugin"

def plugin_function(options):
    print("Running Example Plugin")

# Register the plugin automatically upon module import
manager.register_plugin(PLUGIN_NAME, plugin_function)
