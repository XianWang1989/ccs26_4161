
from package import MODULE1, MODULE2, MODULE3, MODULE4

def main():
    question = input('Please Enter your question: ').lower()

    if MODULE1.check_condition(question):
        MODULE1.play_game()
    elif MODULE2.check_condition(question):
        MODULE2.play_game()
    elif MODULE3.check_condition(question):
        MODULE3.play_game()
    elif MODULE4.check_condition(question):
        MODULE4.play_game()
    else:
        print("No game available for your query.")

if __name__ == "__main__":
    main()
