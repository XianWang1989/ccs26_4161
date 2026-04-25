
from package import *

def main():
    name = input('Please enter your question: ').lower()

    # Check each module's game in order
    if hasattr(MODULE1, 'play_game'):
        MODULE1.play_game(name)

    if hasattr(MODULE2, 'play_game'):
        MODULE2.play_game(name)

    # Add additional checks for MODULE3, MODULE4 as necessary

if __name__ == "__main__":
    main()
