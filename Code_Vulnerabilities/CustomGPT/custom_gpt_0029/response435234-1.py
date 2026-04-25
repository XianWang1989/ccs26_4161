
import os
import importlib
from plugins_manager import Manager

manager = Manager()

def load_plugins():
    plugins_dir = os.path.join(os.path.dirname(__file__), 'plugins')
    for filename in os.listdir(plugins_dir):
        if filename.endswith('.py') and filename != '__init__.py':
            # Import the plugin module
            module_name = f'plugins.{filename[:-3]}'  # Remove .py
            importlib.import_module(module_name)

def main():
    load_plugins()
    print(manager.plugins)

if __name__ == "__main__":
    main()
