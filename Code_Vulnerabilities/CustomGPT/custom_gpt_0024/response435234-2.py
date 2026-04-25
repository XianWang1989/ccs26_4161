
from application import manager

PLUGIN_NAME = "AAC_Player"

def plugin_function(options):
    # Do something relevant to the plugin
    print(f"Running {PLUGIN_NAME}")

# Register the plugin automatically when this module is imported
manager.register_plugin(PLUGIN_NAME, plugin_function)
