
# application.py
import os
import glob
from plugins_manager import Manager

manager = Manager()

# Load all plugins
def load_plugins():
    plugin_dir = 'plugins/*.py'
    for plugin_file in glob.glob(plugin_dir):
        # Import each plugin file
        __import__(plugin_file[:-3].replace('/', '.'))

def main():
    load_plugins()
    print(manager.plugins)

if __name__ == "__main__":
    main()
