
from application import manager

PLUGIN_NAME = "AAC_Player"

def plugin_function(options):
    # Do something when the plugin is used
    pass

# Register the plugin
manager.register_plugin(PLUGIN_NAME, plugin_function)
