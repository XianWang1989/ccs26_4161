
# application.py
from plugins import *  # This automatically registers the plugins

manager = Manager()

def main():
    print(manager.plugins)

main()
