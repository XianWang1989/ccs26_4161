
from package import MODULE1, MODULE2, MODULE3, MODULE4

def main():
    name = input('Please enter your question: ').lower()

    if len(name) >= 3:
        MODULE1.play_game()
    elif len(name) >= 3:
        MODULE2.play_game()
    elif len(name) >= 3:
        MODULE3.play_game()
    # Add more checks as needed for MODULE4

if __name__ == "__main__":
    main()
