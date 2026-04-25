
import os
import pkgutil
from application import manager

# Automatically register all plugins in the plugins directory
def load_plugins():
    package = __name__
    # Iterate over all modules in the current package (plugins)
    for _, module_name, _ in pkgutil.iter_modules([os.path.dirname(__file__)]):
        # Import the plugin by name
        module = __import__(f"{package}.{module_name}", fromlist=[''])
        # If there's a function defined as `plugin_function` in the module, register it
        if hasattr(module, 'plugin_function'):
            plugin_name = getattr(module, 'PLUGIN_NAME', module_name)  # fallback to module name
            manager.register_plugin(plugin_name, module.plugin_function)

load_plugins()  # Call the loading function
