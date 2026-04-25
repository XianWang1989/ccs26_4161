
# application.py

import os
import importlib
from plugins_manager import Manager

manager = Manager()


def load_plugins():
    # Get the path to the plugins directory
    plugins_dir = 'plugins'

    # Iterate through each file in the plugins directory
    for filename in os.listdir(plugins_dir):
        if filename.endswith('.py') and filename != '__init__.py':
            # Import the module
            module_name = f"{plugins_dir}.{filename[:-3]}"  # Strip the '.py' extension
            importlib.import_module(module_name)

def main():
    load_plugins()
    print(manager.plugins)


if __name__ == '__main__':
    main()
