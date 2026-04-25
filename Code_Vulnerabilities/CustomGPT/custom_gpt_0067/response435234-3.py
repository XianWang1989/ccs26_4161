
from application import manager

PLUGIN_NAME = "AAC_Player"

def plugin_function(options):
    # Implement plugin functionality here

def register_plugin(manager):
    manager.register_plugin(PLUGIN_NAME, plugin_function)
