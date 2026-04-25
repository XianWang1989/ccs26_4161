
import os
import importlib
from plugins_manager import Manager

manager = Manager()

def load_plugins():
    plugins_dir = 'plugins'
    for module_name in os.listdir(plugins_dir):
        if module_name.endswith('.py') and module_name != '__init__.py':
            import_path = f"{plugins_dir}.{module_name[:-3]}"
            importlib.import_module(import_path)

def main():
    load_plugins()
    print(manager.plugins)

if __name__ == "__main__":
    main()
