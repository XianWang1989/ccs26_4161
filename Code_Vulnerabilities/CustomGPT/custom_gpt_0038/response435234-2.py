
from plugins_manager import manager

def main():
    manager.load_plugins('plugins')  # Load plugins from the directory
    print(manager.plugins)

if __name__ == "__main__":
    main()
