
import os
import importlib
from plugins_manager import Manager

manager = Manager()

def load_plugins():
    plugins_dir = 'plugins'
    for filename in os.listdir(plugins_dir):
        if filename.endswith('.py') and filename != '__init__.py':
            plugin_name = filename[:-3]  # Remove .py extension
            module = importlib.import_module(f'{plugins_dir}.{plugin_name}')
            # Assuming each plugin has a `register` function to call
            if hasattr(module, 'register'):
                module.register(manager)

def main():
    load_plugins()
    print(manager.plugins)

if __name__ == "__main__":
    main()
