
# application.py

from plugins import plugin1
from plugins import plugin2
from plugins import example_plugin
# Explicitly import each plugin module to run their top-level code.

manager = Manager()

def main():
    print(manager.plugins)  # Print registered plugins

if __name__ == "__main__":
    main()
