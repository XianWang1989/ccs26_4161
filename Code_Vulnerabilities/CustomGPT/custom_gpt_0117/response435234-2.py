
from application import manager

PLUGIN_NAME = "AAC_Player"

def plugin_function(options):
    # do something

# Automatically register plugin when this file is imported
manager.register_plugin(PLUGIN_NAME, plugin_function)
