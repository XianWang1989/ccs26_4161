
import os
import glob
from application import manager

# Dynamically import all .py files in the current directory (excluding __init__.py)
plugin_files = glob.glob(os.path.join(os.path.dirname(__file__), "*.py"))
for plugin_file in plugin_files:
    if not plugin_file.endswith("__init__.py"):
        plugin_name = os.path.basename(plugin_file)[:-3]  # Remove .py extension
        __import__(f'plugins.{plugin_name}')
