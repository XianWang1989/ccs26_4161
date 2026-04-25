
import os
import pkgutil
from plugins_manager import Manager

manager = Manager()

def load_plugins():
    # Dynamically import all modules in the plugins directory
    package = 'plugins'
    for _, name, _ in pkgutil.iter_modules([package]):
        module = __import__(f"{package}.{name}", fromlist=['init'])
        if hasattr(module, 'init'):
            module.init(manager)

def main():
    load_plugins()
    print(manager.plugins)

if __name__ == "__main__":
    main()
