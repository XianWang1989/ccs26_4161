
# application.py
from plugins import load_plugins  # Import the load_plugins function

manager = Manager()

def main():
    load_plugins()  # Load and register all plugins
    print(manager.plugins)  # Now this will print registered plugins

main()
