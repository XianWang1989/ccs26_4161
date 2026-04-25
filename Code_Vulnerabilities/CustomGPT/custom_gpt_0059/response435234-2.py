
from application import manager

PLUGIN_NAME = "AAC_Player"

def plugin_function(options):
    print("Playing AAC...")

manager.register_plugin(PLUGIN_NAME, plugin_function)
