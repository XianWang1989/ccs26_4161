
# plugins/__init__.py

from application import manager
import pkgutil
import importlib

# Auto-register all plugins
def auto_register():
    package_name = 'plugins'
    package = importlib.import_module(package_name)

    for module_info in pkgutil.iter_modules(package.__path__):
        if module_info.name != "__init__":
            module = importlib.import_module(f"{package_name}.{module_info.name}")
            if hasattr(module, 'plugin_function'):
                manager.register_plugin(module.PLUGIN_NAME, module.plugin_function)

auto_register()
