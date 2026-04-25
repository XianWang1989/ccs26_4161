
from application import manager

PLUGIN_NAME = "AAC_Player"

def plugin_function(options):
    # Your plugin logic here
    print(f"{PLUGIN_NAME} is doing something.")

# Automatically register the plugin when imported.
manager.register_plugin(PLUGIN_NAME, plugin_function)
