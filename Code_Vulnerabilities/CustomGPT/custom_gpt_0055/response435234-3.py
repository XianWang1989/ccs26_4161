
from application import manager

PLUGIN_NAME = "AAC_Player"

def plugin_function(options):
    # do something

# Register with the manager when this module is imported
manager.register_plugin(PLUGIN_NAME, plugin_function)
