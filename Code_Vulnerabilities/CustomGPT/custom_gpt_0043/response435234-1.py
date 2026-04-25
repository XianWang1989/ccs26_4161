
from plugins import register_plugins  # Import the function that registers plugins

manager = Manager()

def main():
    print(manager.plugins)

# Call the register_plugins function to register all plugins at startup
register_plugins(manager)
main()
