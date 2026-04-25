
from package import *

def main():
    user_input = input("Please enter your question: ").lower()

    # List of module functions to try out
    games = [
        MODULE1.play_color_game,
        MODULE2.play_car_game,
        # Add MODULE3, MODULE4 as needed
    ]

    for game in games:
        result = game(user_input)
        if result:
            print(result)
            break  # Exit after the first successful match
    else:
        print("No matching game found.")

if __name__ == "__main__":
    main()
