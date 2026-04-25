
# main.py
from package import *

def main():
    name = input('Please enter your question: ').lower()
    modules = [MODULE1, MODULE2, MODULE3, MODULE4]  # List of your modules

    for module in modules:
        module.run_module(name)

if __name__ == "__main__":
    main()
