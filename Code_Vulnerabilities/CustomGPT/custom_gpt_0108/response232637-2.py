
# main.py
from package import *

def main():
    name = input('Please enter your question: ').lower()

    # Check MODULE1
    if len(name) >= 3:
        MODULE1.play_game(name)
    elif len(name) >= 3:
        MODULE2.another_game(name)
    elif len(name) >= 3:
        MODULE3.yet_another_game(name)
    # Continue for other modules

if __name__ == '__main__':
    main()
