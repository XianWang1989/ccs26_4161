
import os
import importlib

class Manager(object):
    def __init__(self):
        self.plugins = {}

    def register_plugin(self, name, plugin_func):
        self.plugins[name] = plugin_func

    def load_plugins(self, plugins_dir):
        for filename in os.listdir(plugins_dir):
            if filename.endswith('.py') and filename != '__init__.py':
                module_name = filename[:-3]
                importlib.import_module(f'plugins.{module_name}')

# In application.py
manager = Manager()

def main():
    # Load plugins from the directory
    manager.load_plugins('plugins')
    print(manager.plugins)

main()
