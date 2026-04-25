
from plugins_manager import Manager

manager = Manager()

# Load plugins from the plugins directory
manager.load_plugins('plugins')

def main():
    print(manager.plugins)

if __name__ == "__main__":
    main()
