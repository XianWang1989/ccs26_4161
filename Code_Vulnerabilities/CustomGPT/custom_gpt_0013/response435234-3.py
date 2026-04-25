
from plugins import register_plugins

# Initialize the Manager instance globally
manager = Manager()

def main():
    register_plugins()  # This will register all plugins
    print(manager.plugins)

main()
