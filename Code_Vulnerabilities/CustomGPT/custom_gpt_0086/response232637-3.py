
# main.py
from package.MODULE1 import play_color_game
from package.MODULE2 import play_car_game
# Import other modules as needed

def main():
    question = input('Please enter your question: ').lower()

    if 'color' in question:
        play_color_game()
    elif 'car' in question:
        play_car_game()
    # Add more conditions for additional modules

if __name__ == "__main__":
    main()
