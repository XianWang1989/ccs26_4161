
# plugins_manager.py
class Manager(object):

    def __init__(self):
        self.plugins = {}

    def register_plugin(self, name, plugin_func):
        self.plugins[name] = plugin_func


# application.py
import importlib
import os
import pkgutil
from plugins_manager import Manager

# Initialize the global Manager instance
manager = Manager()

def load_plugins():
    # Dynamically load all plugin modules in the plugins directory
    for _, module_name, _ in pkgutil.iter_modules(['plugins']):
        module = importlib.import_module(f'plugins.{module_name}')

def main():
    load_plugins()  # Load and register plugins
    print(manager.plugins)  # Display registered plugins

if __name__ == "__main__":
    main()


# plugins/plugin1.py
from application import manager

PLUGIN_NAME = "AAC_Player"

def plugin_function(options):
    # Implement plugin functionality here
    print("AAC Player Plugin Functionality")

# Register the plugin automatically
manager.register_plugin(PLUGIN_NAME, plugin_function)


# plugins/plugin2.py
from application import manager

PLUGIN_NAME = "MP3_Player"

def plugin_function(options):
    # Implement plugin functionality here
    print("MP3 Player Plugin Functionality")

# Register the plugin automatically
manager.register_plugin(PLUGIN_NAME, plugin_function)
