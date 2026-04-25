
from application import manager

PLUGIN_NAME = "AAC_Player"

def plugin_function(options):
    # do something
    print(f"Plugin {PLUGIN_NAME} loaded!")

# Automatically register the plugin when this module is loaded
manager.register_plugin(PLUGIN_NAME, plugin_function)
