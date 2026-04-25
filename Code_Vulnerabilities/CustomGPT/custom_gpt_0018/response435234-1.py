
import os
import importlib

class Manager(object):
    def __init__(self):
        self.plugins = {}

    def register_plugin(self, name, plugin_func):
        self.plugins[name] = plugin_func

    def load_plugins(self, plugins_dir):
        # Iterate over the plugin directory and import each plugin module
        for filename in os.listdir(plugins_dir):
            if filename.endswith('.py') and filename != '__init__.py':
                plugin_name = filename[:-3]  # Remove .py extension
                module = importlib.import_module(f'plugins.{plugin_name}')
                if hasattr(module, 'register'):
                    module.register(self)
