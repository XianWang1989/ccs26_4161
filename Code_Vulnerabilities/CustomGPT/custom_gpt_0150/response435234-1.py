
import os
import importlib

class Manager:
    def __init__(self):
        self.plugins = {}

    def register_plugin(self, name, plugin_func):
        self.plugins[name] = plugin_func

    def load_plugins(self, plugins_dir):
        for plugin_file in os.listdir(plugins_dir):
            if plugin_file.endswith(".py") and plugin_file != "__init__.py":
                module_name = plugin_file[:-3]  # Remove .py extension
                importlib.import_module(f'plugins.{module_name}')
