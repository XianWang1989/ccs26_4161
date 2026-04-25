
from package import *

def main():
    name = input('Please Enter your question: ').lower()
    if len(name) >= 3:  # Check if input is valid
        MODULE1.play_color_game(name)
        MODULE2.play_car_game(name)
        # Call more modules as needed

if __name__ == "__main__":
    main()
