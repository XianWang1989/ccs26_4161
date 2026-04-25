
from application import manager

PLUGIN_NAME = "AAC_Player"

def plugin_function(options):
    # Plugin functionality here
    print("AAC Player loaded")

# Register the plugin
manager.register_plugin(PLUGIN_NAME, plugin_function)
