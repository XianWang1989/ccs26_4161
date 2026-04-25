
import os
import importlib
from plugins_manager import Manager

manager = Manager()

def load_plugins():
    plugins_dir = os.path.join(os.path.dirname(__file__), 'plugins')
    for filename in os.listdir(plugins_dir):
        if filename.endswith('.py') and not filename.startswith('__'):
            module_name = filename[:-3]  # Strip '.py' extension
            importlib.import_module(f'plugins.{module_name}')

def main():
    load_plugins()
    print(manager.plugins)

if __name__ == "__main__":
    main()
