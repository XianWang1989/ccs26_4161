
from application import manager

PLUGIN_NAME = "MP3_Player"

def plugin_function(options):
    # Implement plugin functionality
    pass

# Automatic registration of the plugin
manager.register_plugin(PLUGIN_NAME, plugin_function)
