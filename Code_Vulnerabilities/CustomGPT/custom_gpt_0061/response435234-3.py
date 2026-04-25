
from application import manager

PLUGIN_NAME = "AAC_Player"

def plugin_function(options):
    # do something
    pass

# Automatically register the plugin upon import
manager.register_plugin(PLUGIN_NAME, plugin_function)
