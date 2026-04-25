
# application.py
from plugins import *  # This will trigger all plugins to register themselves

manager = Manager()

def main():
    # The manager.plugins will now contain all registered plugins
    print(manager.plugins)

if __name__ == "__main__":
    main()
