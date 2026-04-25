
import os
import glob
from plugins_manager import Manager

manager = Manager()

# Function to load all plugins
def load_plugins():
    plugin_files = glob.glob(os.path.join("plugins", "*.py"))
    for plugin_file in plugin_files:
        # Import the plugin module
        __import__(plugin_file[:-3].replace('/', '.'))

def main():
    load_plugins()
    print(manager.plugins)

if __name__ == "__main__":
    main()
