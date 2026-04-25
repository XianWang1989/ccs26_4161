
from application import manager

PLUGIN_NAME = "AAC_Player"

def plugin_function(options):
    # Plugin logic here
    print("AAC Player Loaded")

# Automatically register the plugin upon importing
manager.register_plugin(PLUGIN_NAME, plugin_function)
