
from application import manager

PLUGIN_NAME = "Another_Plugin"

def plugin_function(options):
    # Do something

manager.register_plugin(PLUGIN_NAME, plugin_function)
