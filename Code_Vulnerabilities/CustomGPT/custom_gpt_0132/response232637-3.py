
from package import MODULE1, MODULE2, MODULE3, MODULE4

def main():
    name = input('Please Enter your question: ').lower()

    if MODULE1.play_game():  # Call MODULE1's function
        return
    elif MODULE2.play_game():  # Call MODULE2's function
        return
    elif MODULE3.play_game():  # Call MODULE3's function
        return
    elif MODULE4.play_game():  # Call MODULE4's function
        return

    print("No relevant module found for the question.")

if __name__ == "__main__":
    main()
