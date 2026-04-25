
# application.py
from plugins import load_plugins

manager = Manager()

# Load plugins at startup
load_plugins()

def main():
    print(manager.plugins)

main()
