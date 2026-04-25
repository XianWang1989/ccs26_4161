
from package import *

def main():
    name = input('Please Enter your question: ').lower()
    name2 = name.split()

    # Try all modules in sequence
    for module in [MODULE1, MODULE2]:
        module.play_game(name2)

if __name__ == '__main__':
    main()
