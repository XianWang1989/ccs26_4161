
from application import manager

PLUGIN_NAME = "AAC_Player"

def plugin_function(options):
    # Do something specific to this plugin
    print(f"Running {PLUGIN_NAME} with options: {options}")

manager.register_plugin(PLUGIN_NAME, plugin_function)  # This will be unnecessary now but keeps it explicit
