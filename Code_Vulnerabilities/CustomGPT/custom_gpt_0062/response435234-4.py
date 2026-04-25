
import pkgutil

def register_plugins():
    # Automatically find and register all plugins in the directory
    package_name = __name__
    for _, module_name, _ in pkgutil.iter_modules([__path__[0]]):
        module = __import__(f"{package_name}.{module_name}", fromlist=["plugin_function"])
        manager.register_plugin(module_name, module.plugin_function)
