
# plugins/plugin1.py
from application import manager

PLUGIN_NAME = "AAC_Player"

def plugin_function(options):
    # do something with options here
    print("AAC Player Plugin activated.")

manager.register_plugin(PLUGIN_NAME, plugin_function)  # This will be called when the module is imported.
