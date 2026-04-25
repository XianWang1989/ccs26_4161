
from plugins_manager import Manager

manager = Manager()

def load_plugins():
    # Importing all plugin modules to ensure they register themselves
    import plugins.plugin1
    import plugins.plugin2
    import plugins.example_plugin
    # You can dynamically load all plugins in the plugins directory here too

def main():
    load_plugins()
    print(manager.plugins)

if __name__ == "__main__":
    main()
