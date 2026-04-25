
# application.py
import os
import importlib
from plugins_manager import Manager

manager = Manager()

def load_plugins():
    plugins_dir = 'plugins'
    for filename in os.listdir(plugins_dir):
        if filename.endswith('.py') and not filename.startswith('_'):
            importlib.import_module(f'{plugins_dir}.{filename[:-3]}')

def main():
    load_plugins()
    print(manager.plugins)

if __name__ == '__main__':
    main()
