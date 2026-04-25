
import os
import pkgutil
from plugins_manager import Manager

manager = Manager()

def load_plugins():
    # Dynamically load all plugins from the 'plugins' directory
    package = 'plugins'
    for _, module_name, _ in pkgutil.iter_modules([package]):
        module = __import__(f"{package}.{module_name}", fromlist=[''])
        if hasattr(module, 'register'):
            module.register(manager)

def main():
    load_plugins()
    print(manager.plugins)

if __name__ == "__main__":
    main()
