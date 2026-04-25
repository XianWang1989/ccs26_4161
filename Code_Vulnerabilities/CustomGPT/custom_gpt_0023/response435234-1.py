
# plugin1.py
from application import manager

PLUGIN_NAME = "AAC_Player"

def plugin_function(options):
    # do something

# Register the plugin automatically upon import
manager.register_plugin(PLUGIN_NAME, plugin_function)
