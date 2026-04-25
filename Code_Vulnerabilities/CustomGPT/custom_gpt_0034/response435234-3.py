
from plugins import *  # This will trigger the imports in __init__.py

manager = Manager()

def main():
    print(manager.plugins)

main()
