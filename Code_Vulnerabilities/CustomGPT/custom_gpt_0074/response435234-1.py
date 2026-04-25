
# plugins/__init__.py

import os
import importlib
from application import manager

# Get the directory of the current file (the plugins directory)
plugin_dir = os.path.dirname(__file__)

# Loop over all files in the plugin directory
for filename in os.listdir(plugin_dir):
    # Check if it is a Python file and skip __init__.py
    if filename.endswith('.py') and filename != '__init__.py':
        # Construct the module name from the filename
        module_name = f"plugins.{filename[:-3]}"  # Strip .py extension
        # Import the plugin module
        module = importlib.import_module(module_name)
        # If the module has a register function, call it
        if hasattr(module, 'register_plugin'):
            module.register_plugin(manager)

# Now all plugins are registered when `plugins` is imported
