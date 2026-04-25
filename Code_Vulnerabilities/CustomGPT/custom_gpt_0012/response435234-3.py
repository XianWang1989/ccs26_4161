
from application import manager

PLUGIN_NAME = "MP3_Player"

def plugin_function(options):
    # do something

# Register the plugin when this module is imported
manager.register_plugin(PLUGIN_NAME, plugin_function)
