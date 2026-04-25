
import os
import importlib
from plugins_manager import Manager

manager = Manager()

def load_plugins():
    plugins_dir = 'plugins'
    for filename in os.listdir(plugins_dir):
        if filename.endswith('.py') and filename != '__init__.py':
            module_name = filename[:-3]  # Remove .py extension
            importlib.import_module(f'plugins.{module_name}')

    # Optionally, you can also print the loaded plugins for confirmation
    print(f"Loaded plugins: {list(manager.plugins.keys())}")

def main():
    load_plugins()  # Load and register all plugins
    print(manager.plugins)  # Display registered plugins

if __name__ == "__main__":
    main()
