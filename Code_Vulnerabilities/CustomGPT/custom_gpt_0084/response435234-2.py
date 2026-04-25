
# plugins/plugin1.py
from application import manager

PLUGIN_NAME = "AAC_Player"

def plugin_function(options):
    # Plugin logic here
    print("Plugin function called")

manager.register_plugin(PLUGIN_NAME, plugin_function)
