
import os
import glob
from plugins_manager import Manager

manager = Manager()

# Automatically import all plugin modules
plugin_files = glob.glob(os.path.join("plugins", "*.py")) + glob.glob(os.path.join("plugins", "*/", "*.py"))

for plugin in plugin_files:
    module_name = os.path.splitext(os.path.basename(plugin))[0]
    __import__(f'plugins.{module_name}')

def main():
    print(manager.plugins)

main()
