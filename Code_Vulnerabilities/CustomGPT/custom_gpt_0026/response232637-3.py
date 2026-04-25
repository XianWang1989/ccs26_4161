
from package import *

def main():
    name = input('Please enter your question: ').lower()

    # Check each module in sequence
    modules = [MODULE1, MODULE2]  # Add more modules as needed
    for module in modules:
        if hasattr(module, 'play_color_game') and len(name) >= 3:
            module.play_color_game(name)
            break
        elif hasattr(module, 'play_car_game') and len(name) >= 3:
            module.play_car_game(name)
            break

if __name__ == "__main__":
    main()
