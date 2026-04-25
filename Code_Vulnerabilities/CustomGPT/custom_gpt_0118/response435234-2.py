
# plugins/plugin1.py
from application import manager

PLUGIN_NAME = "AAC_Player"

def plugin_function(options):
    # Do something specific to this plugin
    pass

def register(manager_instance):
    manager_instance.register_plugin(PLUGIN_NAME, plugin_function)
