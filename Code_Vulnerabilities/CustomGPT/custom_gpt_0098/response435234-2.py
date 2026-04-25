
from application import manager

PLUGIN_NAME = "AAC_Player"

def plugin_function(options):
    # Plugin logic here
    print("Plugin function executed with options:", options)

manager.register_plugin(PLUGIN_NAME, plugin_function)
