
import os
import importlib.util
from plugins_manager import Manager

manager = Manager()

def load_plugins():
    plugins_dir = 'plugins'
    for filename in os.listdir(plugins_dir):
        if filename.endswith('.py') and filename != '__init__.py':
            module_name = filename[:-3]
            # Load the module
            module_path = os.path.join(plugins_dir, filename)
            spec = importlib.util.spec_from_file_location(module_name, module_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            # Automatically register the plugin
            if hasattr(module, 'plugin_function'):
                manager.register_plugin(module.PLUGIN_NAME, module.plugin_function)

def main():
    load_plugins()
    print(manager.plugins)

if __name__ == "__main__":
    main()
