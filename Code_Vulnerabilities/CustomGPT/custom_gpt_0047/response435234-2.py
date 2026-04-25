
import os
import importlib
import pkgutil
from plugins_manager import manager

def load_plugins():
    # Get the directory of the plugins
    plugin_dir = os.path.join(os.path.dirname(__file__), 'plugins')

    # Loop through all plugin modules
    for _, module_name, _ in pkgutil.iter_modules([plugin_dir]):
        importlib.import_module(f'plugins.{module_name}')

def main():
    load_plugins()
    print(manager.plugins)

if __name__ == "__main__":
    main()
