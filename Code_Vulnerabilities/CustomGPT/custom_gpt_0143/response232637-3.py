
from package import MODULE1, MODULE2, MODULE3, MODULE4

def main():
    question = input('Please enter your question: ').lower()

    if len(question) >= 3:
        MODULE1.play_game(question)
    if len(question) >= 3:
        MODULE2.play_game(question)
    if len(question) >= 3:
        MODULE3.play_game(question)
    if len(question) >= 3:
        MODULE4.play_game(question)

if __name__ == "__main__":
    main()
