
# main.py
from package import *

def run_game(name):
    if MODULE1.play_game(name):
        return
    if MODULE2.play_game(name):
        return
    if MODULE3.play_game(name):
        return
    # Add more modules as needed

if __name__ == "__main__":
    user_input = input('Please enter your question: ').lower()
    run_game(user_input)
