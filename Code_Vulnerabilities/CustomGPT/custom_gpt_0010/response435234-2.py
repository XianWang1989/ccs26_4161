
import os
import glob
from plugins_manager import Manager

manager = Manager()

def load_plugins():
    # Load all plugins in the plugins directory
    plugin_files = glob.glob(os.path.join('plugins', '*.py'))
    for file in plugin_files:
        # Import the plugin module dynamically
        __import__(os.path.basename(file)[:-3])  # Exclude the .py extension

def main():
    load_plugins()
    print(manager.plugins)

if __name__ == "__main__":
    main()
