
import os
import importlib

class Manager(object):
    def __init__(self):
        self.plugins = {}

    def register_plugin(self, name, plugin_func):
        self.plugins[name] = plugin_func

    def load_plugins(self):
        # Get the directory of the plugins
        plugins_dir = os.path.join(os.path.dirname(__file__), 'plugins')
        # Loop through all files in the plugins directory
        for filename in os.listdir(plugins_dir):
            if filename.endswith('.py') and filename != '__init__.py':
                # Dynamically import the plugin module
                module_name = filename[:-3]  # Remove the .py extension
                importlib.import_module(f'plugins.{module_name}')
