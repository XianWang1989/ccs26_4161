
# main.py
from package import *

def main():
    name = input('Please Enter your question: ').lower()
    name2 = name.split()  # Split input into words

    # Check each module's game
    if len(name2) >= 3:
        MODULE1.play_color_game(name)
    if len(name2) >= 3:
        MODULE2.play_car_game(name)

if __name__ == "__main__":
    main()
