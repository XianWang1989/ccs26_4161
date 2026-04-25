
import os
import importlib
import pkgutil
from plugins_manager import Manager

manager = Manager()

def load_plugins():
    plugin_dir = 'plugins'
    # Iterate over all modules in the plugins directory
    for _, module_name, _ in pkgutil.iter_modules([plugin_dir]):
        importlib.import_module(f"{plugin_dir}.{module_name}")

def main():
    load_plugins()  # Load and register plugins
    print(manager.plugins)

if __name__ == "__main__":
    main()
