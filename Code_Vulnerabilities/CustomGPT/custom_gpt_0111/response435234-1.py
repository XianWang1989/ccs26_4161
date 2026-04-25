
import os
import glob
from plugins_manager import Manager

manager = Manager()

# Automatically import all plugin modules
plugin_files = glob.glob('plugins/*.py')
for plugin in plugin_files:
    __import__(os.path.splitext(os.path.basename(plugin))[0])

def main():
    print(manager.plugins)

main()
