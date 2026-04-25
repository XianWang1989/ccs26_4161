
from application import manager

PLUGIN_NAME = "MP3_Player"

def plugin_function(options):
    # Plugin logic here
    pass

# Automatically register the plugin upon import
manager.register_plugin(PLUGIN_NAME, plugin_function)
