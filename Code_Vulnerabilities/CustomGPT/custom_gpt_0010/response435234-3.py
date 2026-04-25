
from application import manager

PLUGIN_NAME = "AAC_Player"

def plugin_function(options):
    # Implementation of the plugin
    print(f"{PLUGIN_NAME} is doing something.")

# Automatically register the plugin upon import
manager.register_plugin(PLUGIN_NAME, plugin_function)
