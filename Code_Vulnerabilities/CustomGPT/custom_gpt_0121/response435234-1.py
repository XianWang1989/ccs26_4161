
import os
import pkgutil
import importlib
from application import manager

# Dynamically register all plugins
def register_plugins():
    package = __name__
    path = package.split('.')

    for _, module_name, is_pkg in pkgutil.iter_modules(path):
        if not is_pkg:  # Only import modules, not sub-packages
            module = importlib.import_module(f"{package}.{module_name}")
            if hasattr(module, 'plugin_function'):
                manager.register_plugin(module.PLUGIN_NAME, module.plugin_function)

# Call the registration function
register_plugins()
