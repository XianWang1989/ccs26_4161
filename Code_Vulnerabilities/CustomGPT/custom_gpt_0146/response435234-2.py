
from application import manager

PLUGIN_NAME = "AAC_Player"

def plugin_function(options):
    # Example functionality
    return "Playing AAC file..."

# Automatically register the plugin upon import
manager.register_plugin(PLUGIN_NAME, plugin_function)
