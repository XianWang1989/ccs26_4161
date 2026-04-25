
from application import manager

PLUGIN_NAME = "AAC_Player"

def plugin_function(options):
    print("AAC Player is now playing.")

manager.register_plugin(PLUGIN_NAME, plugin_function)
