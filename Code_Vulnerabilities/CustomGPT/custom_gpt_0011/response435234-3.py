
from plugins import *  # This will import everything from __init__.py

manager = Manager()

def main():
    print(manager.plugins)

if __name__ == "__main__":
    main()
