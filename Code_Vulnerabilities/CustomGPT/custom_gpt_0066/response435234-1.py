
# plugin1.py
from application import manager

PLUGIN_NAME = "AAC_Player"

def plugin_function(options):
    # placeholder for plugin functionality
    pass

# Automatic registration upon import
manager.register_plugin(PLUGIN_NAME, plugin_function)
