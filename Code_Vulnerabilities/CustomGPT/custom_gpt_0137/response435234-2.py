
from application import manager

PLUGIN_NAME = "AAC_Player"

def plugin_function(options):
    # Implementation of the plugin functionality
    pass

# Automatically register the plugin when the file is imported
manager.register_plugin(PLUGIN_NAME, plugin_function)
