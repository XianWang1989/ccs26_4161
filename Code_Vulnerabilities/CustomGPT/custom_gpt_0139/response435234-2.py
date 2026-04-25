
# application.py
from plugins_manager import Manager

manager = Manager()

# Import all plugins to register them
import plugins.plugin1
import plugins.plugin2
import plugins.example_plugin
# Add more plugin imports as needed

def main():
    print(manager.plugins)

if __name__ == "__main__":
    main()
