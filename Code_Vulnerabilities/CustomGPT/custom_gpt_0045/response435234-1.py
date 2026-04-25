
# plugins/__init__.py
import pkgutil
import importlib

# Import the Manager instance from the application
from application import manager

def load_plugins():
    # Loop over all modules in the 'plugins' package
    package = __name__  # current package name for relative imports
    for _, module_name, _ in pkgutil.iter_modules([__path__[0]]):
        # Import each plugin module
        importlib.import_module(f"{package}.{module_name}")

load_plugins()
