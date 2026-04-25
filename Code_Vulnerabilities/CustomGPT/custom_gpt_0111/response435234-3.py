
from application import manager

PLUGIN_NAME = "MP3_Player"

def plugin_function(options):
    # Plugin functionality here
    print("MP3 Player loaded")

# Register the plugin
manager.register_plugin(PLUGIN_NAME, plugin_function)
