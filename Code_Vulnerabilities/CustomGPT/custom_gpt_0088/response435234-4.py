
import os
import importlib

manager = Manager()

# Dynamically load plugins from the plugins directory
plugin_dir = 'plugins'
for filename in os.listdir(plugin_dir):
    if filename.endswith('.py') and filename != '__init__.py':
        module_name = f"{plugin_dir.replace('/', '.')}.{filename[:-3]}"
        importlib.import_module(module_name)

def main():
    print(manager.plugins)

main()
