
from package import MODULE1, MODULE2

def main():
    name = input('Please enter your question: ').lower()

    # Call MODULE1's game
    MODULE1.play_game(name)

    # If MODULE1 didn't handle the input, check MODULE2
    if not any(color in name for color in ['red', 'green', 'blue']):
        MODULE2.play_game(name)

    # Add further modules as needed...

if __name__ == "__main__":
    main()
