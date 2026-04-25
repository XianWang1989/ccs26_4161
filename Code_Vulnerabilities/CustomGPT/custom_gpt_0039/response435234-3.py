
from application import manager

PLUGIN_NAME = "AAC_Player"

def plugin_function(options):
    # Do something specific for the AAC player
    pass

# Register the plugin.
manager.register_plugin(PLUGIN_NAME, plugin_function)
