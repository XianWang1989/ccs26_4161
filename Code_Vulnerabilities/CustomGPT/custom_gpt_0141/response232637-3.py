
# main.py
from package import *

name = input('Please enter your question: ').lower()

# Define a function to handle game logic
def run_game(name):
    # Attempt to run each module in order
    if not MODULE1.run_color_game(name):
        if not MODULE2.run_car_game(name):
            print("No matching game found for your input.")

# Run the game with user input
run_game(name)
