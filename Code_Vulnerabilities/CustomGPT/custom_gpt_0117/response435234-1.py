
import os
import importlib.util

from plugins_manager import Manager

manager = Manager()

def load_plugins():
    plugins_dir = os.path.join(os.path.dirname(__file__), 'plugins')

    for filename in os.listdir(plugins_dir):
        if filename.endswith('.py') and filename != '__init__.py':
            module_name = filename[:-3]  # Strip .py extension
            file_path = os.path.join(plugins_dir, filename)
            spec = importlib.util.spec_from_file_location(module_name, file_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

# Load plugins at startup
load_plugins()

def main():
    print(manager.plugins)

if __name__ == "__main__":
    main()
