
from plugins import plugin1
from plugins import plugin2
# Import other plugins as needed

manager = Manager()

def main():
    print(manager.plugins)  # This will now show the registered plugins

main()
