
# In plugin1.py

from application import manager

PLUGIN_NAME = "AAC_Player"

def plugin_function(options):
    # Some implementation code here
    pass

def register_plugin(manager_instance):
    manager_instance.register_plugin(PLUGIN_NAME, plugin_function)
