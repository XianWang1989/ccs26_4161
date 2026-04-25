
import os
import importlib.util
import pkgutil
from plugins_manager import Manager

manager = Manager()

def load_plugins(plugins_directory):
    for _, module_name, _ in pkgutil.iter_modules([plugins_directory]):
        module_path = os.path.join(plugins_directory, module_name)
        if os.path.isdir(module_path):
            # If it's a directory, we can load `__init__.py` or any specific modules
            load_plugins(module_path)  # Recursive call to load sub-modules
        else:
            # Import the plugin module
            spec = importlib.util.spec_from_file_location(module_name, module_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)  # Execute the module to register the plugin

def main():
    # Load plugins from the plugins directory
    load_plugins('plugins')

    # Now you could print or use the registered plugins
    print(manager.plugins)

if __name__ == "__main__":
    main()
