
from plugins_manager import manager

PLUGIN_NAME = "AAC_Player"

def plugin_function(options):
    # Plugin functionality here
    return "Plugin Running"

manager.register_plugin(PLUGIN_NAME, plugin_function)
