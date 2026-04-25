
import pkgutil
import importlib
from plugins_manager import Manager

manager = Manager()

# Automatically register plugins from the plugins package
def load_plugins():
    package = 'plugins'
    for _, module_name, _ in pkgutil.iter_modules([package]):
        importlib.import_module(f'{package}.{module_name}')

load_plugins()

def main():
    print(manager.plugins)

if __name__ == "__main__":
    main()
