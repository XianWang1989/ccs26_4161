
import os
import importlib.util

from plugins_manager import Manager

manager = Manager()

def load_plugins():
    plugins_dir = 'plugins'
    for filename in os.listdir(plugins_dir):
        if filename.endswith('.py') and filename != '__init__.py':
            plugin_name = filename[:-3]  # Remove .py extension

            # Import the plugin module
            module_path = os.path.join(plugins_dir, filename)
            spec = importlib.util.spec_from_file_location(plugin_name, module_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

def main():
    load_plugins()
    print(manager.plugins)

if __name__ == '__main__':
    main()
