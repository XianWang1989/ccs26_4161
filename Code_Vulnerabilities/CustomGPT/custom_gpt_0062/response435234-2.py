
from plugins import register_plugins

manager = Manager()

# Call to register all plugins
register_plugins()

def main():
    print(manager.plugins)

main()
