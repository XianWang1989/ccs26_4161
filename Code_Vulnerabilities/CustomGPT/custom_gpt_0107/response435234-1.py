
import os
import glob
from plugins_manager import Manager

manager = Manager()

def load_plugins():
    plugin_dir = 'plugins'
    # Use glob to find all plugin files
    for plugin_file in glob.glob(os.path.join(plugin_dir, '*.py')):
        if not plugin_file.endswith('__init__.py'):
            # Import the plugin module
            module_name = os.path.splitext(os.path.basename(plugin_file))[0]
            __import__(f'plugins.{module_name}')

def main():
    load_plugins()
    print(manager.plugins)

if __name__ == "__main__":
    main()
