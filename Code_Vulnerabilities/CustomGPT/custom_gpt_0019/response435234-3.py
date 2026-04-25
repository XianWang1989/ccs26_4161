
import os
import importlib

from plugins_manager import Manager

manager = Manager()

# Dynamic loading of all plugins
def load_plugins():
    plugins_dir = 'plugins'
    for filename in os.listdir(plugins_dir):
        if filename.endswith('.py') and filename != '__init__.py':
            importlib.import_module(f'plugins.{filename[:-3]}')  # Import the plugin module

def main():
    load_plugins()  # Load and register all plugins
    print(manager.plugins)  # Display registered plugins

main()
