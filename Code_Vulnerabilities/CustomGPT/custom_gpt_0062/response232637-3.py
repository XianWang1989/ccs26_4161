
from package import MODULE1, MODULE2, MODULE3, MODULE4

def main():
    name = input('Please Enter your question: ').lower()

    if len(name) >= 3:
        MODULE1.play_game(name)  # Call the function from MODULE1
    else:
        MODULE2.play_game(name)  # Call the function from MODULE2

if __name__ == "__main__":
    main()
