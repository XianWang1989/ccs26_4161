
from application import manager

PLUGIN_NAME = "AAC_Player"

def plugin_function(options):
    # Plugin functionality here
    pass

manager.register_plugin(PLUGIN_NAME, plugin_function)
