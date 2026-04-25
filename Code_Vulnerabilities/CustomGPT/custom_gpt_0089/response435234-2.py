
import os
import importlib
import pkgutil
from plugins_manager import Manager

manager = Manager()

def load_plugins():
    plugins_dir = os.path.join(os.path.dirname(__file__), 'plugins')

    # Iterate through all modules in the plugins directory
    for _, module_name, _ in pkgutil.iter_modules(['plugins']):
        importlib.import_module(f'plugins.{module_name}')

def main():
    load_plugins()
    print(manager.plugins)

if __name__ == '__main__':
    main()
