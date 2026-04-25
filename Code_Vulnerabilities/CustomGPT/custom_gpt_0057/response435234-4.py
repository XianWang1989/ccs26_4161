
# plugins_manager.py
class Manager(object):
    def __init__(self):
        self.plugins = {}

    def register_plugin(self, name, plugin_func):
        self.plugins[name] = plugin_func

manager = Manager()

# application.py
import os
import importlib
from plugins_manager import manager

def load_plugins():
    plugins_dir = 'plugins'
    for filename in os.listdir(plugins_dir):
        if filename.endswith('.py') and not filename.startswith('__'):
            importlib.import_module(f'{plugins_dir}.{filename}')

def main():
    load_plugins()
    print(manager.plugins)

if __name__ == '__main__':
    main()

# plugins/plugin1.py
from plugins_manager import manager

PLUGIN_NAME = "AAC_Player"

def plugin_function(options):
    return "Plugin Running"

manager.register_plugin(PLUGIN_NAME, plugin_function)
