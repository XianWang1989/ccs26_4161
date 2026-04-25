
import os
import glob
from plugins import *  # This will import all plugins in the plugins directory

manager = Manager()

def main():
    print(manager.plugins)

if __name__ == "__main__":
    main()
