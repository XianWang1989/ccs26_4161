
from plugins_manager import manager

def main():
    # Load plugins upon starting the application
    manager.load_plugins('plugins')
    print(manager.plugins)

if __name__ == "__main__":
    main()
