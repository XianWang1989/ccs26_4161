
from application import manager

PLUGIN_NAME = "AAC_Player"

def plugin_function(options):
    # Plugin functionality goes here
    print(f"{PLUGIN_NAME} is doing something!")

# This line automatically registers the plugin at module import time
manager.register_plugin(PLUGIN_NAME, plugin_function)
