
# main.py
from package.module1 import run_color_game
from package.module2 import run_car_game
# Import other modules similarly...

def main():
    name = input('Please enter your question: ').lower()

    if len(name) >= 3:
        run_color_game(name)
        run_car_game(name)
        # Call other module functions as needed

if __name__ == "__main__":
    main()
