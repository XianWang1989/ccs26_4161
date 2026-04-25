
import os
import importlib
from plugins_manager import Manager

manager = Manager()

def load_plugins():
    plugin_dir = 'plugins'
    for filename in os.listdir(plugin_dir):
        if filename.endswith('.py') and filename != '__init__.py':
            module_name = filename[:-3]  # Strip off .py
            importlib.import_module(f"{plugin_dir}.{module_name}")

def main():
    load_plugins()
    print(manager.plugins)

if __name__ == "__main__":
    main()
