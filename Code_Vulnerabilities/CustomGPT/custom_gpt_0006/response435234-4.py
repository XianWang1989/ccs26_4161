
# plugins/__init__.py
import os
import importlib

plugin_dir = os.path.dirname(__file__)

for filename in os.listdir(plugin_dir):
    if filename.endswith('.py') and filename != '__init__.py':
        importlib.import_module(f'plugins.{filename[:-3]}')  # Exclude the .py extension
