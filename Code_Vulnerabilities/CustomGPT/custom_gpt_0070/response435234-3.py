
from application import manager

PLUGIN_NAME = "AAC_Player"

def plugin_function(options):
    print(f"Running plugin with options: {options}")

manager.register_plugin(PLUGIN_NAME, plugin_function)
