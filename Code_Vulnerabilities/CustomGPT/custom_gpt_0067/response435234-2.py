
import os
import importlib
from plugins_manager import Manager

manager = Manager()

def load_plugins():
    plugins_dir = 'plugins'
    for module_name in os.listdir(plugins_dir):
        if module_name.endswith('.py') and module_name != '__init__.py':
            module_path = f"{plugins_dir}.{module_name[:-3]}"  # Remove .py
            module = importlib.import_module(module_path)
            # Each plugin file should call register_plugin in its own global scope
            if hasattr(module, 'register_plugin'):
                module.register_plugin(manager)

def main():
    load_plugins()
    print(manager.plugins)

if __name__ == "__main__":
    main()
