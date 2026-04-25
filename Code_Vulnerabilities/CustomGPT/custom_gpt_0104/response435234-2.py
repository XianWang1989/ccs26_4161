
from plugins import plugin1  # Importing plugin1 implicitly registers it
from plugins import plugin2  # Importing plugin2
from plugins import example_plugin  # Importing example_plugin

manager = Manager()

def main():
    print(manager.plugins)

if __name__ == "__main__":
    main()
