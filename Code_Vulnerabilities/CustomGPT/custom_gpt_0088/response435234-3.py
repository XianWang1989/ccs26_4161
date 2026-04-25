
from plugins import plugin1  # Will execute plugin1.py
from plugins import plugin2  # Will execute plugin2.py

manager = Manager()

def main():
    print(manager.plugins)

main()
