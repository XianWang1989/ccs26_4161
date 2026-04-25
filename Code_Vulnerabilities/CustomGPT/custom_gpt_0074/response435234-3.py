
# application.py
from plugins import *  # This will trigger the registration of all the plugins

manager = Manager()

def main():
    print(manager.plugins)

main()
