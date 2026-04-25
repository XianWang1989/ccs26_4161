
from application import manager

PLUGIN_NAME = "AAC_Player"

def plugin_function(options):
    # Implement plugin functionality here
    print(f"{PLUGIN_NAME} is running with options: {options}")

manager.register_plugin(PLUGIN_NAME, plugin_function)
