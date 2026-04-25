
import os
import importlib.util

class Manager:
    def __init__(self):
        self.plugins = {}

    def register_plugin(self, name, plugin_func):
        self.plugins[name] = plugin_func

    def load_plugins(self, plugins_dir):
        for filename in os.listdir(plugins_dir):
            if filename.endswith('.py') and filename != '__init__.py':
                module_name = filename[:-3]  # Strip .py extension
                module_path = os.path.join(plugins_dir, filename)

                # Load the module
                spec = importlib.util.spec_from_file_location(module_name, module_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

                # Register the plugin using its predefined PLUGIN_NAME
                if hasattr(module, 'PLUGIN_NAME') and hasattr(module, 'plugin_function'):
                    self.register_plugin(module.PLUGIN_NAME, module.plugin_function)
