
from plugins import *  # This will execute all imports in __init__.py

manager = Manager()

def main():
    print("Registered Plugins:", manager.plugins)

main()
