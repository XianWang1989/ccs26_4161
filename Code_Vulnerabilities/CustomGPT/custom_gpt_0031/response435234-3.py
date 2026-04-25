
from application import manager

PLUGIN_NAME = "AAC_Player"

def plugin_function(options):
    # Plugin functionality here
    print(f"Plugin {PLUGIN_NAME} loaded with options: {options}")

# Automatically register the plugin
manager.register_plugin(PLUGIN_NAME, plugin_function)
