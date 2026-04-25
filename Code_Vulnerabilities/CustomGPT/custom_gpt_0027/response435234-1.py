
from plugins import plugin1, plugin2, example_plugin
from plugins_manager import Manager

manager = Manager()

def main():
    print(manager.plugins)

if __name__ == "__main__":
    main()
