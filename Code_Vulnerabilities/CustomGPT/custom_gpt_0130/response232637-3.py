
# main.py
from package import *

def main():
    while True:
        question = input('Please enter your question or type "exit" to quit: ').lower()
        if question == "exit":
            break

        # Call MODULE1
        MODULE1.play_game()

        # Call MODULE2 only if MODULE1 didn't handle it
        MODULE2.play_game()
        # Add more calls for MODULE3, MODULE4, etc., as needed

if __name__ == "__main__":
    main()
