
from package import *

def main():
    question = input('Please enter your question: ').lower()

    # Try each module's game one by one
    for module in [MODULE1, MODULE2, MODULE3, MODULE4]:
        module.play_game(question)

if __name__ == "__main__":
    main()
