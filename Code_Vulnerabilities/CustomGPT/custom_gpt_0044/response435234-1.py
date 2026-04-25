
import os
import importlib.util

class Manager(object):

    def __init__(self, plugins_dir):
        self.plugins = {}
        self.load_plugins(plugins_dir)

    def register_plugin(self, name, plugin_func):
        self.plugins[name] = plugin_func

    def load_plugins(self, plugins_dir):
        for filename in os.listdir(plugins_dir):
            if filename.endswith(".py") and filename != "__init__.py":
                module_name = filename[:-3]  # Remove .py extension
                self.load_plugin_module(module_name)

    def load_plugin_module(self, module_name):
        # Import the plugin module and register it
        module_path = os.path.join('plugins', module_name)
        spec = importlib.util.spec_from_file_location(module_name, f"{module_path}.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        # Assume each plugin has a function called 'plugin_function'
        if hasattr(module, 'plugin_function'):
            self.register_plugin(module.PLUGIN_NAME, module.plugin_function)


# Initialize global Manager instance
manager = Manager('plugins')

def main():
    print(manager.plugins)

if __name__ == "__main__":
    main()
