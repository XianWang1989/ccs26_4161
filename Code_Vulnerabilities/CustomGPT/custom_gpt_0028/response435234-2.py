
from application import manager

PLUGIN_NAME = "AAC_Player"

def plugin_function(options):
    # Plugin functionality here
    print("Plugin function executed with options:", options)

# Register the plugin with the manager
manager.register_plugin(PLUGIN_NAME, plugin_function)
