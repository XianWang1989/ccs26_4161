
from application import manager

PLUGIN_NAME = "AAC_Player"

def plugin_function(options):
    # Perform plugin action
    print("AAC Player plugin loaded.")

# Register the plugin when the module is imported
manager.register_plugin(PLUGIN_NAME, plugin_function)
