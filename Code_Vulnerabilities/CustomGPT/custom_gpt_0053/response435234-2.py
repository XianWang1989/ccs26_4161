
import os
import importlib

# Assuming your structure is as you described
PLUGIN_DIR = 'plugins'

# Initialize Manager instance globally
manager = Manager()

def load_plugins():
    # Loop through the plugin directory and import all modules
    for filename in os.listdir(PLUGIN_DIR):
        if filename.endswith('.py') and filename != '__init__.py':
            module_name = filename[:-3]  # Remove .py extension
            importlib.import_module(f"{PLUGIN_DIR}.{module_name}")

def main():
    load_plugins()  # Load and register plugins
    print(manager.plugins)  # Display registered plugins

if __name__ == "__main__":
    main()
