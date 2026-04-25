
from plugins_manager import manager

PLUGIN_NAME = "AAC_Player"

def plugin_function(options):
    # do something

# Auto-register on import
manager.register_plugin(PLUGIN_NAME, plugin_function)
