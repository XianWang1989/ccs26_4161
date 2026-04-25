
import os
import glob
from plugins_manager import Manager

manager = Manager()

def load_plugins():
    plugin_dir = 'plugins/*.py'  # Adjust the glob pattern as needed
    for filepath in glob.glob(plugin_dir):
        __import__(os.path.basename(filepath)[:-3])  # Import each plugin module

def main():
    load_plugins()
    print(manager.plugins)

if __name__ == "__main__":
    main()
