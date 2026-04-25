
from application import manager

PLUGIN_NAME = "AAC_Player"

def plugin_function(options):
    # do something

# Automatically register the plugin when the module is imported
manager.register_plugin(PLUGIN_NAME, plugin_function)
