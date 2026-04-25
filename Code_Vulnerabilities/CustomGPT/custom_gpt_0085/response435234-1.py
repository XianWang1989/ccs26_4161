
from plugins_manager import Manager

manager = Manager()

def main():
    print(manager.plugins)

# Automatically import all plugins from the plugins directory
import_plugins()

def import_plugins():
    import pkgutil
    import plugins  # This will locate the plugins package

    for _, module_name, _ in pkgutil.iter_modules(plugins.__path__):
        __import__(f'plugins.{module_name}')

main()
