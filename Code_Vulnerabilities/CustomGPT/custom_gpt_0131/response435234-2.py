
from application import manager

PLUGIN_NAME = "AAC_Player"

def plugin_function(options):
    # Plugin functionality goes here
    print(f"{PLUGIN_NAME} is executing.")

# Register the plugin automatically
manager.register_plugin(PLUGIN_NAME, plugin_function)
