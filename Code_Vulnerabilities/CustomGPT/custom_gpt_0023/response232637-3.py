
# main.py
from package.MODULE1 import play_game as play_game1
from package.MODULE2 import play_game as play_game2
from package.MODULE3 import play_game as play_game3
from package.MODULE4 import play_game as play_game4

def main():
    name = input('Please Enter your question: ').strip().lower()

    # Use a list to define the order of module checks
    modules = [play_game1, play_game2, play_game3, play_game4]

    for play_game in modules:
        play_game(name)  # Call the function from the module
        # You can break if the game was successfully triggered

if __name__ == "__main__":
    main()
