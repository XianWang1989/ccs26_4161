
from package import MODULE1, MODULE2, MODULE3, MODULE4

def main():
    name = input('Please Enter your question: ').lower()

    # Call functions based on the input
    if MODULE1.play_game() is None:
        if MODULE2.play_game() is None:
            if MODULE3.play_game() is None:
                MODULE4.play_game()

if __name__ == '__main__':
    main()
