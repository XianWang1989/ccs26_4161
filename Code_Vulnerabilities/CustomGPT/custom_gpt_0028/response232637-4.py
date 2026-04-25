
from package import *

def main():
    question = input('Please Enter your question: ').lower()

    # Try each module in turn
    for module in [MODULE1, MODULE2, MODULE3]:
        module.play_game(question)

if __name__ == "__main__":
    main()
