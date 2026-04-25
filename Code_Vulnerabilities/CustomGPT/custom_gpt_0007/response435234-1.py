
import os
import importlib

class Manager(object):
    def __init__(self):
        self.plugins = {}

    def register_plugin(self, name, plugin_func):
        self.plugins[name] = plugin_func

# Automatically load all plugins on initialization
def load_plugins(manager):
    plugins_dir = os.path.dirname(os.path.abspath(__file__)) + "/plugins"
    for filename in os.listdir(plugins_dir):
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = filename[:-3]
            importlib.import_module(f'plugins.{module_name}')

# Create the manager instance
manager = Manager()
load_plugins(manager)
