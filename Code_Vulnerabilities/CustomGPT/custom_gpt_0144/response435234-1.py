# application.py
import importlib.util
import os
import sys
from plugins_manager import Manager

manager = Manager()

def load_plugins():
    plugins_dir = os.path.join(os.path.dirname(__file__), 'plugins')

    for root, _, files in os.walk(plugins_dir):
        for file in files:
            if file.endswith('.py') and file != '__init__.py':
                plugin_path = os.path.join(root, file)
                module_name = os.path.relpath(plugin_path, os.path.dirname(__file__)).replace(os.sep, '.').replace('.py', '')

                spec = importlib.util.spec_from_file_location(module_name, plugin_path)
                module = importlib.util.module_from_spec(spec)
                sys.modules[module_name] = module
                spec.loader.exec_module(module)

def main():
    load_plugins()
    print("Registered Plugins:", manager.plugins)

if __name__ == "__main__":
    main()
