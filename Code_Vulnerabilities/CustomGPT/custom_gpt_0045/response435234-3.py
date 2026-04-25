
# application.py
from plugins import load_plugins

manager = Manager()

def main():
    load_plugins()  # Load and register plugins
    print(manager.plugins)  # This should now show registered plugins

if __name__ == "__main__":
    main()
