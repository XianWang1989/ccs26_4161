
from application import manager

PLUGIN_NAME = "AAC_Player"

def plugin_function(options):
    # do something
    print(f"{PLUGIN_NAME} function called!")

manager.register_plugin(PLUGIN_NAME, plugin_function)
