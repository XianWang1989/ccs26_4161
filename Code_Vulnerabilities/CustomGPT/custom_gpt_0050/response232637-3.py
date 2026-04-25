
from package import MODULE1, MODULE2

def main():
    name = input('Please enter your question: ').lower()

    # Check MODULE1
    MODULE1.play_game(name)

    # Check MODULE2 if MODULE1 doesn't match
    if name not in ['what is my color', 'color']:  # Example condition for MODULE1
        MODULE2.play_game(name)

if __name__ == "__main__":
    main()
