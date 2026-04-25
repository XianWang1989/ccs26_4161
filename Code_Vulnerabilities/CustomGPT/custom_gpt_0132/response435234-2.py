
from plugins_manager import Manager
import os

manager = Manager()

def main():
    # Load plugins from the plugins directory
    manager.load_plugins('plugins')
    print(manager.plugins)

main()
