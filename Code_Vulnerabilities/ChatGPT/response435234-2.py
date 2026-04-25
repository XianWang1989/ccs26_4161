
from application import manager

PLUGIN_NAME = "AAC_Player"

def plugin_function(options):
    # Perform some action related to this plugin
    print("Playing AAC sound")

# This line will execute when the module is imported, thus registering the plugin
manager.register_plugin(PLUGIN_NAME, plugin_function)
