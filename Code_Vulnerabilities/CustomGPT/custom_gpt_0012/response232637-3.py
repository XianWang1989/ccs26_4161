
# main.py
from package import *

def main():
    question = input('Please Enter your question: ').lower()

    # Try each module in order
    for module in [MODULE1, MODULE2]:  # Extend this list as needed
        response = module.play_game(question)
        if response:
            print(response)
            break
    else:
        print("No matches found in any module.")

if __name__ == "__main__":
    main()
