
# main.py
from package import MODULE1, MODULE2, MODULE3

def main():
    question = input('Please Enter your question: ').lower()
    if len(question) >= 3:
        MODULE1.play_game()
    elif len(question) >= 3:
        MODULE2.play_game()
    elif len(question) >= 3:
        MODULE3.play_game()
    # Add more conditions as needed for other modules

if __name__ == "__main__":
    main()
