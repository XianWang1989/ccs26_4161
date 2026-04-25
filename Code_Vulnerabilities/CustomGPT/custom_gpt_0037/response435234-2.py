
from application import manager

PLUGIN_NAME = "AAC_Player"

def plugin_function(options):
    # Plugin logic here
    pass

# Automatically register the plugin when this module is loaded
manager.register_plugin(PLUGIN_NAME, plugin_function)
