
from plugins_manager import Manager

manager = Manager()

def main():
    # Load and register plugins at startup
    manager.load_plugins()
    print(manager.plugins)

if __name__ == '__main__':
    main()
