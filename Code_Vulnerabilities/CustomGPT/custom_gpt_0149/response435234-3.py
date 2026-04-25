
from plugins_manager import Manager
import plugins  # This imports all plugins and runs the registration

manager = Manager()

def main():
    print(manager.plugins)

if __name__ == "__main__":
    main()
