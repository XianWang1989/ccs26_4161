
import os
import importlib

def load_plugins():
    plugins_dir = 'plugins'
    for filename in os.listdir(plugins_dir):
        if filename.endswith('.py') and not filename.startswith('__'):
            module_name = f"{plugins_dir}.{filename[:-3]}"
            importlib.import_module(module_name)

load_plugins()
