
from application import manager

PLUGIN_NAME = "MP3_Player"

def plugin_function(options):
    print(f"Plugin {PLUGIN_NAME} loaded.")

manager.register_plugin(PLUGIN_NAME, plugin_function)
