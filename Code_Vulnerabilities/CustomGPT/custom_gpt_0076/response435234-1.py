
import os
import importlib.util

class Manager(object):
    def __init__(self):
        self.plugins = {}
        self.load_plugins()

    def register_plugin(self, name, plugin_func):
        self.plugins[name] = plugin_func

    def load_plugins(self):
        plugins_dir = 'plugins'
        for filename in os.listdir(plugins_dir):
            if filename.endswith('.py') and not filename.startswith('__'):
                self.load_plugin(filename)

    def load_plugin(self, filename):
        module_name = filename[:-3]  # remove .py extension
        module_path = os.path.join('plugins', filename)
        spec = importlib.util.spec_from_file_location(module_name, module_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
