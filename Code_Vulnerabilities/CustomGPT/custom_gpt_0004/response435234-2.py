
# application.py
from plugins import manager  # Make sure plugins are registered

def main():
    print(manager.plugins)

if __name__ == "__main__":
    main()
