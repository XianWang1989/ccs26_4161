
# application.py

import os
import importlib
from plugins_manager import Manager

manager = Manager()

def load_plugins():
    # Load all Python files in the plugins directory
    plugin_dir = 'plugins'
    for filename in os.listdir(plugin_dir):
        if filename.endswith('.py') and filename != '__init__.py':
            module_name = f'{plugin_dir}.{filename[:-3]}'
            importlib.import_module(module_name)

def main():
    load_plugins()  # Load plugins at startup
    print(manager.plugins)

if __name__ == "__main__":
    main()
