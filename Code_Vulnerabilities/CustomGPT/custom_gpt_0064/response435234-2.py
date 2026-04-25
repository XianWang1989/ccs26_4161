
from application import manager

PLUGIN_NAME = "AAC_Player"

def plugin_function(options):
    # Implement plugin functionality here
    pass

# Auto-register plugin on import
manager.register_plugin(PLUGIN_NAME, plugin_function)
