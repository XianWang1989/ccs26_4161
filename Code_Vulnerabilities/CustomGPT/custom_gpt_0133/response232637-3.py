
from package import *

def main():
    # Assuming you have a function in each module called play_game
    name_input = input('Please enter your question: ').lower()

    # Call MODULE1's game
    MODULE1.play_game()  # This will run MODULE1

    # Check if specific conditions aren't met, and then call MODULE2
    if not any(item in name_input for item in ['what is my color', 'color']):
        MODULE2.play_game()

    # Add checks for MODULE3, MODULE4 similarly
    # Each call to a module can be based on the failed conditions or user input.

if __name__ == "__main__":
    main()
