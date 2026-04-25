
import os
import importlib
from application import manager

# Automatically register all plugins in this folder
plugin_folder = os.path.dirname(__file__)
for filename in os.listdir(plugin_folder):
    if filename.endswith('.py') and not filename.startswith('__'):
        # Import each plugin file
        module_name = filename[:-3]  # Remove the .py extension
        plugin_module = importlib.import_module(f'plugins.{module_name}')
