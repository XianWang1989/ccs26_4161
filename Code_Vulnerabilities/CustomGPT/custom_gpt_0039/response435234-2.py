
from plugins_manager import Manager

manager = Manager()

def main():
    manager.load_plugins('plugins')
    print(manager.plugins)

main()
