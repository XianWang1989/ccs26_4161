
from application import manager
import pkgutil

# Automatically find and register all plugins in this directory
def register_plugins():
    package_name = __name__
    for _, module_name, is_pkg in pkgutil.iter_modules(__path__):
        if not is_pkg:  # Only import modules, not packages
            module = __import__(f"{package_name}.{module_name}", fromlist=[None])
            # Assuming each module has a PLUGIN_NAME and a plugin_function defined
            if hasattr(module, 'PLUGIN_NAME') and hasattr(module, 'plugin_function'):
                manager.register_plugin(module.PLUGIN_NAME, module.plugin_function)

register_plugins()
