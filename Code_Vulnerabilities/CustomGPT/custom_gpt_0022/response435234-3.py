
from application import manager

PLUGIN_NAME = "AAC_Player"

def plugin_function(options):
    # Do something

# Automatically register the plugin
manager.register_plugin(PLUGIN_NAME, plugin_function)
