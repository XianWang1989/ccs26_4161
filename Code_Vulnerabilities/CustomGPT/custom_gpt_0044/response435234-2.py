
from application import manager

PLUGIN_NAME = "Example_Plugin"

def plugin_function(options):
    # do something
    print(f"Running {PLUGIN_NAME}")

manager.register_plugin(PLUGIN_NAME, plugin_function)
