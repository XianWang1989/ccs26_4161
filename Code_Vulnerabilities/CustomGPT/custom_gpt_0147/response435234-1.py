
import os
import importlib

class Manager:
    def __init__(self):
        self.plugins = {}

    def register_plugin(self, name, plugin_func):
        self.plugins[name] = plugin_func

    def load_plugins(self, plugins_directory):
        for filename in os.listdir(plugins_directory):
            if filename.endswith('.py') and filename != '__init__.py':
                module_name = filename[:-3]  # Remove .py extension
                module = importlib.import_module(f'plugins.{module_name}')
