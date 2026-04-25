
import os
import pkgutil
from plugins_manager import Manager

manager = Manager()

def load_plugins():
    plugin_dir = 'plugins'
    for module_info in pkgutil.iter_modules([plugin_dir]):
        module_name = module_info.name
        module = __import__(f'{plugin_dir}.{module_name}', fromlist=[''])
        # Optionally, anything else you need to do with the module

def main():
    load_plugins()
    print(manager.plugins)

if __name__ == '__main__':
    main()
