
from application import manager

PLUGIN_NAME = "AAC_Player"

def plugin_function(options):
    # Implementation for the plugin
    print("AAC Player functionality")

# Register the plugin during import
manager.register_plugin(PLUGIN_NAME, plugin_function)
