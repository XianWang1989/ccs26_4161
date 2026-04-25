
from application import manager

PLUGIN_NAME = "AAC_Player"

def plugin_function(options):
    # Placeholder for plugin functionality
    pass

def init(manager):
    manager.register_plugin(PLUGIN_NAME, plugin_function)
