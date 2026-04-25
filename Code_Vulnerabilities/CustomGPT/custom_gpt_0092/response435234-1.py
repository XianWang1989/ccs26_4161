
import os
import importlib
from application import manager

# Automatically load all plugins
def load_plugins():
    plugin_dir = os.path.dirname(__file__)
    for filename in os.listdir(plugin_dir):
        if filename.endswith('.py') and filename != '__init__.py':
            module_name = filename[:-3]  # Remove '.py'
            importlib.import_module(f'plugins.{module_name}')

load_plugins()
