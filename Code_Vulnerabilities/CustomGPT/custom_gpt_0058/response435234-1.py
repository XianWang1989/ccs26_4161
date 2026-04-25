
import os
import pkgutil
import importlib
from plugins_manager import Manager

manager = Manager()

def load_plugins():
    # Define the plugins directory
    plugins_dir = "plugins"

    # Loop through modules in the plugins directory
    for loader, module_name, is_pkg in pkgutil.iter_modules([plugins_dir]):
        # Import the module
        module = importlib.import_module(f"{plugins_dir}.{module_name}")

# Load plugins automatically at startup
load_plugins()

def main():
    print(manager.plugins)

main()
