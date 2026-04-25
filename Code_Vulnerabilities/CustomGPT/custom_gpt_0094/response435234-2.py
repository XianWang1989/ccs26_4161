
# plugins/plugin1.py

from application import manager

PLUGIN_NAME = "AAC_Player"

def plugin_function(options):
    # Plugin implementation goes here
    pass

# Register the plugin on import
manager.register_plugin(PLUGIN_NAME, plugin_function)
