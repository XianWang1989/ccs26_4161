
# application.py
import os
import importlib.util

# Assuming you've defined the Manager class in plugins_manager.py
from plugins_manager import Manager  

# Initialize Manager instance globally
manager = Manager()

def load_plugins():
    plugins_dir = os.path.join(os.path.dirname(__file__), 'plugins')
    for plugin_file in os.listdir(plugins_dir):
        if plugin_file.endswith('.py') and plugin_file != '__init__.py':
            plugin_path = os.path.join(plugins_dir, plugin_file)
            spec = importlib.util.spec_from_file_location(plugin_file[:-3], plugin_path)
            plugin_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(plugin_module)  # This imports the module and runs its code

def main():
    load_plugins()
    print(manager.plugins)

if __name__ == '__main__':
    main()
