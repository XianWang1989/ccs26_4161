
import os
import importlib
import plugins_manager

# Initialize the global Manager instance
manager = plugins_manager.Manager()

def load_plugins():
    # Specify the plugins directory
    plugins_dir = 'plugins'

    # Iterate over each file in the plugins directory
    for filename in os.listdir(plugins_dir):
        # Ignore non-Python files and the __init__.py file
        if filename.endswith('.py') and filename != '__init__.py':
            # Create a module name by removing the .py extension
            module_name = f"{plugins_dir}.{filename[:-3]}"
            # Import the plugin module
            importlib.import_module(module_name)

def main():
    load_plugins()
    print(manager.plugins)

main()
