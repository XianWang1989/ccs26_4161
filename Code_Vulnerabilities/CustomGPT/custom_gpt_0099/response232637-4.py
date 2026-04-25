
from package import *

def main():
    question = input('Please enter your question: ').lower()

    if len(question) >= 3:
        MODULE1.play_color_game()
    else:
        MODULE2.play_car_game()
        MODULE3.play_food_game()  # Add more checks as needed

if __name__ == "__main__":
    main()
