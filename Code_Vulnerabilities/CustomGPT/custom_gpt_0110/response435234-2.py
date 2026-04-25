
# application.py
import os
import glob
from plugins import *

manager = Manager()

# Import all plugins to register them automatically
plugin_files = glob.glob(os.path.join('plugins', '*.py'))
for plugin in plugin_files:
    __import__(plugin[:-3].replace('/', '.'), fromlist=[''])

def main():
    print(manager.plugins)

main()
