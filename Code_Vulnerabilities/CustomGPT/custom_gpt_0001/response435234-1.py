
import os
import importlib.util

class Manager(object):
    def __init__(self):
        self.plugins = {}
        self.load_plugins()

    def register_plugin(self, name, plugin_func):
        self.plugins[name] = plugin_func

    def load_plugins(self):
        # Iterate through all the files in the plugins directory
        plugins_dir = os.path.join(os.path.dirname(__file__), 'plugins')
        for filename in os.listdir(plugins_dir):
            if filename.endswith('.py') and filename != '__init__.py':
                self.load_plugin(filename)

    def load_plugin(self, filename):
        # Import the plugin module by filename
        module_name = filename[:-3]  # Strip the .py extension
        module_path = os.path.join('plugins', filename)
        spec = importlib.util.spec_from_file_location(module_name, module_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        # Assuming each plugin has a `plugin_function`
        if hasattr(module, 'plugin_function'):
            # Call the register_plugin method with appropriate parameters
            plugin_name = getattr(module, 'PLUGIN_NAME', module_name)  # Use the filename if PLUGIN_NAME is not defined
            self.register_plugin(plugin_name, module.plugin_function)

