
import os
import importlib

# Initialize the Manager instance globally
from plugins_manager import Manager

manager = Manager()

def load_plugins():
    plugin_dir = "plugins"
    # Iterate through all files in the plugins directory
    for module_name in os.listdir(plugin_dir):
        if module_name.endswith(".py") and module_name != "__init__.py":
            importlib.import_module(f"{plugin_dir}.{module_name}")

def main():
    load_plugins()  # Load all plugins
    print(manager.plugins)

main()
