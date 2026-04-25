
import os
import importlib
from plugins_manager import Manager

# Initialize the manager instance globally
manager = Manager()

def load_plugins():
    # Path to the plugins directory
    plugins_dir = 'plugins'

    # Iterate through all files in the plugins directory
    for filename in os.listdir(plugins_dir):
        if filename.endswith('.py') and filename != '__init__.py':
            # Import the module dynamically
            plugin_name = filename[:-3]  # Strip .py extension
            module = importlib.import_module(f'plugins.{plugin_name}')
            print(f'Loaded plugin: {plugin_name}')

def main():
    load_plugins()
    print(manager.plugins)  # This will now show the registered plugins

if __name__ == '__main__':
    main()
