
from application import manager

PLUGIN_NAME = "AAC_Player"

def plugin_function(options):
    print("AAC_Player Plugin: doing something")

manager.register_plugin(PLUGIN_NAME, plugin_function)
