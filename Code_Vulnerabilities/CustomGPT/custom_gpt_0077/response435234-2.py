
from application import manager

PLUGIN_NAME = "AAC_Player"

def plugin_function(options):
    # do something with options here
    print("AAC Player plugin activated.")

manager.register_plugin(PLUGIN_NAME, plugin_function)
