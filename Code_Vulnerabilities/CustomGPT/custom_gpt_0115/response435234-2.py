
from plugins_manager import Manager
import os

manager = Manager()

def load_plugins():
    plugins_dir = os.path.join(os.path.dirname(__file__), 'plugins')
    manager.load_plugins(plugins_dir)

def main():
    load_plugins()  # Load and register plugins
    print(manager.plugins)

if __name__ == "__main__":
    main()
