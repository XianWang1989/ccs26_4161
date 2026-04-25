
from plugins_manager import Manager

manager = Manager()

def main():
    # Load all plugins
    manager.load_plugins('plugins')
    # Print the registered plugins
    print(manager.plugins)

if __name__ == "__main__":
    main()
