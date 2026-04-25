
# application.py
from plugins_manager import Manager

manager = Manager()

# Automatically load and register all plugins
import_plugins = [
    'plugins.plugin1',
    'plugins.plugin2',
    'plugins.example_plugin',
    'plugins.plugin3.player'  # add more as needed
]

for plugin in import_plugins:
    __import__(plugin)

def main():
    print(manager.plugins)

if __name__ == "__main__":
    main()
