
# main.py
from package import *

def main():
    name = input('Please Enter your question: ').lower()
    modules = [MODULE1, MODULE2, MODULE3, MODULE4]  # Add your modules here

    for module in modules:
        if module.game_logic(name):
            break  # Exit if a module's logic is successful

if __name__ == "__main__":
    main()
