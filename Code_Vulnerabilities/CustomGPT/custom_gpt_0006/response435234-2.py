
# application.py
from plugins_manager import Manager

manager = Manager()

# Import plugins to execute their registration code
import plugins  # This will trigger the registration from each plugin

def main():
    print(manager.plugins)

if __name__ == "__main__":
    main()
