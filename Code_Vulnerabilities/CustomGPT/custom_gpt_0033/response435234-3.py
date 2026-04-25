
from application import manager

PLUGIN_NAME = "AAC_Player"

def plugin_function(options):
    # Implement plugin functionality here
    print("AAC_Player is registered.")

# Automatically register the plugin when this module is imported
manager.register_plugin(PLUGIN_NAME, plugin_function)
