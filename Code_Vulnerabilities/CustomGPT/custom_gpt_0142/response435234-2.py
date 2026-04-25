
from plugins import plugin1  # Importing the plugin
from plugins import example_plugin  # Add more as needed

from plugins_manager import Manager

manager = Manager()

def main():
    print(manager.plugins)

if __name__ == "__main__":
    main()
