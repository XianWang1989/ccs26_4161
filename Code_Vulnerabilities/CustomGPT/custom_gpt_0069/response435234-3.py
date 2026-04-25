
import os
import importlib.util

def load_plugins():
    plugin_dir = os.path.dirname(__file__)
    for filename in os.listdir(plugin_dir):
        if filename.endswith('.py') and filename != '__init__.py':
            plugin_name = filename[:-3]  # Remove '.py' extension
            spec = importlib.util.spec_from_file_location(plugin_name, os.path.join(plugin_dir, filename))
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            if hasattr(module, 'plugin_function'):
                manager.register_plugin(plugin_name, module.plugin_function)

# Call this function in your application
load_plugins()
