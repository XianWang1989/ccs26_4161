
# plugin2.py
from application import manager

PLUGIN_NAME = "MP3_Player"

def plugin_function(options):
    # Implement functionality here

manager.register_plugin(PLUGIN_NAME, plugin_function)
