
from application import manager

PLUGIN_NAME = "AAC_Player"

def plugin_function(options):
    # Implementation here

# Register the plugin automatically on import
manager.register_plugin(PLUGIN_NAME, plugin_function)
