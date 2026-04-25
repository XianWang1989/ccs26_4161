
import os
import pkgutil
import importlib

# Automatically import all plugins in the current directory
def register_plugins(manager):
    package = __name__
    for _, module_name, _ in pkgutil.iter_modules([os.path.dirname(__file__)]):
        importlib.import_module(f"{package}.{module_name}")

# Call this function to register plugins
register_plugins(manager)
