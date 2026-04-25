
from plugins import *  # This triggers the import of all plugins and their registration

manager = Manager()

def main():
    print(manager.plugins)

if __name__ == "__main__":
    main()
