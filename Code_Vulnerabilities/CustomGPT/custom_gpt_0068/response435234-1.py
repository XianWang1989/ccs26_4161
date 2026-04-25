
# plugin1.py
from application import manager

PLUGIN_NAME = "AAC_Player"

def plugin_function(options):
    # Implementation of the plugin functionality
    print("Plugin function executed with options:", options)

# Auto-register the plugin when this module is imported
manager.register_plugin(PLUGIN_NAME, plugin_function)
