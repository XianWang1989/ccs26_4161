
from application import manager

PLUGIN_NAME = "AAC_Player"

def plugin_function(options):
    # Implement functionality here
    print(f"Plugin {PLUGIN_NAME} loaded.")

# Register the plugin at import time
manager.register_plugin(PLUGIN_NAME, plugin_function)
