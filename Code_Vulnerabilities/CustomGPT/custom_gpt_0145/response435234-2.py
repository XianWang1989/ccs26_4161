
from application import manager

PLUGIN_NAME = "MP3_Player"

def plugin_function(options):
    # do something

manager.register_plugin(PLUGIN_NAME, plugin_function)
