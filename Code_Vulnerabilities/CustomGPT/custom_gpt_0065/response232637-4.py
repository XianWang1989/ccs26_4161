
from package import *

def main():
    user_input = input('Please enter your question: ').lower()

    # Check MODULE1
    MODULE1.play_color_game(user_input)

    # Check MODULE2 if MODULE1 did not handle it
    MODULE2.play_car_game(user_input)

    # Check MODULE3 if MODULE2 did not handle it
    MODULE3.play_food_game(user_input)

if __name__ == "__main__":
    main()
