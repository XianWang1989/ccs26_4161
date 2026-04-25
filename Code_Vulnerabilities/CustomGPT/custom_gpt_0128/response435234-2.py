
import os
from plugins_manager import Manager

manager = Manager()

def main():
    plugins_dir = os.path.join(os.path.dirname(__file__), 'plugins')
    manager.load_plugins(plugins_dir)
    print(manager.plugins)

if __name__ == '__main__':
    main()
