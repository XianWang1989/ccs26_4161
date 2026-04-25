
# application.py
import pkgutil
import importlib
from plugins_manager import Manager

manager = Manager()

def load_plugins():
    # Iterate over all plugins in the `plugins` directory
    package = 'plugins'  # This should be the name of your plugin directory
    for _, module_name, _ in pkgutil.iter_modules([package]):
        # Import the plugin module
        module = importlib.import_module(f"{package}.{module_name}")
        # Optionally, you can check if the module has a `plugin_function` attribute and more
        if hasattr(module, 'plugin_function'):
            # Register the plugin if it contains the expected function
            manager.register_plugin(module.PLUGIN_NAME, module.plugin_function)

def main():
    load_plugins()  # Load and register all plugins
    print(manager.plugins)

if __name__ == "__main__":
    main()
