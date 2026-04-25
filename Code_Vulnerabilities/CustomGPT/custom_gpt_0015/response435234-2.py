
from application import manager

PLUGIN_NAME = "AAC_Player"

def plugin_function(options):
    # Implementation of the plugin functionality
    print("AAC_Player is performing an action.")

# Automatically register the plugin
manager.register_plugin(PLUGIN_NAME, plugin_function)
