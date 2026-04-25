
import os
import importlib
from plugins_manager import Manager

manager = Manager()

def load_plugins():
    plugins_dir = os.path.dirname(__file__) + '/plugins'
    for filename in os.listdir(plugins_dir):
        if filename.endswith('.py') and filename != '__init__.py':
            importlib.import_module(f'plugins.{filename[:-3]}')

def main():
    load_plugins()
    print(manager.plugins)

if __name__ == '__main__':
    main()
