
# application.py
import os
import importlib
from plugins_manager import Manager

manager = Manager()

# Function to load all plugins
def load_plugins():
    plugins_dir = "plugins"
    for filename in os.listdir(plugins_dir):
        if filename.endswith('.py') and filename != '__init__.py':
            plugin_name = filename[:-3]  # remove .py extension
            importlib.import_module(f"{plugins_dir}.{plugin_name}")

load_plugins()

def main():
    print(manager.plugins)

main()
