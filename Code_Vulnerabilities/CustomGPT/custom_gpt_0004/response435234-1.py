
# plugins/__init__.py
import os
import pkgutil
import importlib
from application import manager

# Automatically register all plugins in the plugins directory
def register_plugins():
    package = __name__
    plugin_dir = os.path.dirname(__file__)

    # Use pkgutil to find all plugins in the package
    for _, module_name, _ in pkgutil.iter_modules([plugin_dir]):
        if module_name != "__init__":
            # Import the module without directly calling it
            importlib.import_module(f"{package}.{module_name}")

register_plugins()
