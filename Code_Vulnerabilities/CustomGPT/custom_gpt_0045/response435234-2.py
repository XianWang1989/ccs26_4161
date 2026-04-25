
# plugins/plugin1.py
from application import manager

PLUGIN_NAME = "AAC_Player"

def plugin_function(options):
    # do something
    print(f"Plugin {PLUGIN_NAME} has been executed.")

# Register the plugin during import
manager.register_plugin(PLUGIN_NAME, plugin_function)
