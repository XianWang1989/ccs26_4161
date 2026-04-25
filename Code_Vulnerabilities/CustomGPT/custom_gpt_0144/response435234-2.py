# plugins/plugin1.py
from application import manager

PLUGIN_NAME = "AAC_Player"

def plugin_function(options):
    print(f"Playing with options: {options}")

manager.register_plugin(PLUGIN_NAME, plugin_function)
