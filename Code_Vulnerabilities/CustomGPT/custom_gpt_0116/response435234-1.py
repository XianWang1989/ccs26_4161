
import os
import glob
from plugins_manager import Manager

manager = Manager()

def load_plugins():
    plugin_folder = 'plugins'
    # Glob all plugin files
    for plugin_file in glob.glob(os.path.join(plugin_folder, '*.py')):
        # Import the plugin module
        module_name = os.path.basename(plugin_file)[:-3]  # Strip .py extension
        __import__(f'plugins.{module_name}')

def main():
    load_plugins()
    print(manager.plugins)

if __name__ == '__main__':
    main()
