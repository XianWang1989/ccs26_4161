
from plugins_manager import Manager
from plugins import register_plugins

manager = Manager()
register_plugins(manager)

def main():
    print(manager.plugins)

if __name__ == "__main__":
    main()
