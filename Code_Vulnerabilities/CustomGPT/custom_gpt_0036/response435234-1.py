
import os
import importlib

class Manager(object):
    def __init__(self):
        self.plugins = {}

    def register_plugin(self, name, plugin_func):
        self.plugins[name] = plugin_func

def load_plugins(manager):
    plugins_dir = 'plugins'
    for plugin_file in os.listdir(plugins_dir):
        if plugin_file.endswith('.py') and plugin_file != '__init__.py':
            # Get the module name by stripping the .py suffix
            module_name = plugin_file[:-3]
            # Import the plugin module
            importlib.import_module(f'{plugins_dir}.{module_name}')

# Initialize Manager instance globally
manager = Manager()

# Automatically load plugins at startup
load_plugins(manager)

def main():
    print(manager.plugins)  # Now this will print the registered plugins

if __name__ == "__main__":
    main()
