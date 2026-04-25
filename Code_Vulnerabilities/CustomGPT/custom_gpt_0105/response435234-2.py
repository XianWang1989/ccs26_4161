
from application import manager

PLUGIN_NAME = "AAC_Player"

def plugin_function(options):
    # do something
    print("AAC_Player plugin function executed.")

manager.register_plugin(PLUGIN_NAME, plugin_function)
