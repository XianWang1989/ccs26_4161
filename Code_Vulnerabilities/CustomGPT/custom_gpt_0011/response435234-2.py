
from application import manager

PLUGIN_NAME = "AAC_Player"

def plugin_function(options):
    # Perform the desired functionality here
    print("Plugin is running with options:", options)

# Automatically register the plugin when this file is imported
manager.register_plugin(PLUGIN_NAME, plugin_function)
