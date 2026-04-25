
import os
import glob
from plugins_manager import Manager

manager = Manager()

def load_plugins():
    plugins_dir = os.path.join(os.path.dirname(__file__), 'plugins')
    plugin_files = glob.glob(os.path.join(plugins_dir, '*.py'))

    # Import each plugin
    for plugin_file in plugin_files:
        module_name = os.path.basename(plugin_file)[:-3]  # Remove .py extension
        __import__(f'plugins.{module_name}')

def main():
    load_plugins()  # Load and register plugins
    print(manager.plugins)

if __name__ == "__main__":
    main()
