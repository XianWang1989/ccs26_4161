
from package import *

def main():
    user_input = input('Please enter your question: ').lower()

    response = MODULE1.play_game(user_input)
    if response is None:
        response = MODULE2.play_game(user_input)
    # Add additional modules as needed
    # elif response is None:
    #     response = MODULE3.play_game(user_input)

    if response:
        print(response)
    else:
        print("Sorry, I don't understand your question.")

if __name__ == "__main__":
    main()
