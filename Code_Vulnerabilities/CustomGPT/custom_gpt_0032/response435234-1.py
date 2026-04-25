
import os
import importlib.util
from pathlib import Path
from plugins_manager import Manager

manager = Manager()

def load_plugins():
    plugins_dir = Path(__file__).resolve().parent / 'plugins'
    for plugin_file in plugins_dir.glob('*.py'):
        module_name = plugin_file.stem
        if module_name != '__init__':
            spec = importlib.util.spec_from_file_location(module_name, plugin_file)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            # Assuming each plugin file contains the necessary registration
            if hasattr(module, 'register'):
                module.register(manager)

def main():
    load_plugins()
    print(manager.plugins)

if __name__ == '__main__':
    main()
