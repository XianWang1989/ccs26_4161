
# application.py
import os
import glob
from plugins_manager import Manager

manager = Manager()

def load_plugins():
    # Load each plugin module
    plugin_files = glob.glob(os.path.join("plugins", "*.py"))
    for plugin_file in plugin_files:
        # Convert file path to module name
        module_name = os.path.basename(plugin_file)[:-3]  # Remove .py
        __import__(f'plugins.{module_name}')  # Import the module

def main():
    load_plugins()  # Load and register all plugins
    print(manager.plugins)

main()
