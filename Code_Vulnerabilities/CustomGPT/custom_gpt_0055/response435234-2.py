
from plugins import register_plugins

manager = Manager()
register_plugins()  # Call the function to register all plugins

def main():
    print(manager.plugins)

main()
