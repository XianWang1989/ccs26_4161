
from application import manager

PLUGIN_NAME = "AAC_Player"

def plugin_function(options):
    # Implement functionality here
    print("AAC Player Functionality")

def register(manager):
    manager.register_plugin(PLUGIN_NAME, plugin_function)
