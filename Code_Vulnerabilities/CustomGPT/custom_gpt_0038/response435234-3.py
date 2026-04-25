
from application import manager

PLUGIN_NAME = "AAC_Player"

def plugin_function(options):
    # Do something
    print("Plugin function called with options:", options)

manager.register_plugin(PLUGIN_NAME, plugin_function)  # This will not be needed anymore in this approach
