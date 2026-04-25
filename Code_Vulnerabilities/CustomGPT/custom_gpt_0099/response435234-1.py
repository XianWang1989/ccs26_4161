
from application import manager
import os
import pkgutil

# Automatically register all plugins
def register_plugins():
    package = __name__
    package_path = os.path.dirname(__file__)

    for _, module_name, _ in pkgutil.iter_modules([package_path]):
        module = __import__(f"{package}.{module_name}", fromlist=[''])
        if hasattr(module, 'plugin_function') and hasattr(module, 'PLUGIN_NAME'):
            manager.register_plugin(module.PLUGIN_NAME, module.plugin_function)

# Register plugins when this module is imported
register_plugins()
