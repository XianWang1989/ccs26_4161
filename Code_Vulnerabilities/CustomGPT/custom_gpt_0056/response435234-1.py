
import os
import importlib
from plugins_manager import Manager

manager = Manager()

def load_plugins(plugin_directory):
    for filename in os.listdir(plugin_directory):
        if filename.endswith('.py') and filename != '__init__.py':
            module_name = filename[:-3]  # Remove .py extension
            importlib.import_module(f'plugins.{module_name}')

def main():
    load_plugins('plugins')
    print(manager.plugins)

if __name__ == '__main__':
    main()
