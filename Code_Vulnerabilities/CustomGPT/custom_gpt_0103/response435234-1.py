
import importlib
import os

class Manager(object):
    def __init__(self):
        self.plugins = {}
        self.load_plugins()

    def register_plugin(self, name, plugin_func):
        self.plugins[name] = plugin_func

    def load_plugins(self):
        plugins_dir = os.path.join(os.path.dirname(__file__), 'plugins')
        for filename in os.listdir(plugins_dir):
            if filename.endswith('.py') and filename != '__init__.py':
                module_name = filename[:-3]  # Strip .py
                importlib.import_module(f'plugins.{module_name}')

