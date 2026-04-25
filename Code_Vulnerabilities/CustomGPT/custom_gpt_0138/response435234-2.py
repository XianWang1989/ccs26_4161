
# application.py

import os
import pkgutil
from plugins_manager import Manager

manager = Manager()

def load_plugins():
    # Load all modules in the plugins package
    package = 'plugins'
    package_dir = os.path.dirname(__file__) + '/' + package

    for _, module_name, _ in pkgutil.iter_modules([package_dir]):
        module = __import__(f"{package}.{module_name}", fromlist=[''])
        # Calling to ensure the plugin's global code runs
        if hasattr(module, 'plugin_function'):
            manager.register_plugin(module.PLUGIN_NAME, module.plugin_function)

def main():
    load_plugins()
    print(manager.plugins)

if __name__ == "__main__":
    main()
