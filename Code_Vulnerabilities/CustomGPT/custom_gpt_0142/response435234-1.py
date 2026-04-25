
from application import manager

PLUGIN_NAME = "AAC_Player"

def plugin_function(options):
    # Plugin functionality goes here
    print(f"{PLUGIN_NAME} plugin function called with options: {options}")

# This line gets executed on import
manager.register_plugin(PLUGIN_NAME, plugin_function)
