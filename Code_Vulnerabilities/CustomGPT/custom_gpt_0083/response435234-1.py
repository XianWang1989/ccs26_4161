
from application import manager

PLUGIN_NAME = "AAC_Player"

def plugin_function(options):
    # Implement functionality here
    print("Plugin function executed")

# Register the plugin when the module is imported
manager.register_plugin(PLUGIN_NAME, plugin_function)
