
import os
import glob
from plugins import *  # This will import all modules in the plugins package
from plugins_manager import Manager

manager = Manager()

# Automatically register plugins when modules are imported
def register_plugins():
    for plugin in glob.glob(os.path.join("plugins", "*.py")):
        # Remove the '.py' extension and the path, only keep the module name
        module_name = os.path.basename(plugin)[:-3]
        __import__(f'plugins.{module_name}')

register_plugins()

def main():
    print(manager.plugins)

if __name__ == "__main__":
    main()
