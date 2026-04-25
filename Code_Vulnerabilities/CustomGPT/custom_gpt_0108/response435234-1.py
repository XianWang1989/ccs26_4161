
# application.py
import os
import importlib
from plugins_manager import Manager

manager = Manager()

def load_plugins():
    plugins_dir = 'plugins'
    for filename in os.listdir(plugins_dir):
        if filename.endswith('.py') and filename != '__init__.py':
            module_name = filename[:-3]  # Strip .py
            importlib.import_module(f"{plugins_dir}.{module_name}")

load_plugins()

def main():
    print(manager.plugins)

if __name__ == "__main__":
    main()
