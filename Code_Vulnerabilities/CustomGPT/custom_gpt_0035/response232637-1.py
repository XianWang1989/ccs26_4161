
# main.py
from package import MODULE1, MODULE2, MODULE3, MODULE4

def play_game(question):
    # Check in MODULE1
    if MODULE1.check_question(question):
        return MODULE1.answer_question()

    # Check in MODULE2
    elif MODULE2.check_question(question):
        return MODULE2.answer_question()

    # Check in MODULE3
    elif MODULE3.check_question(question):
        return MODULE3.answer_question()

    # Check in MODULE4
    elif MODULE4.check_question(question):
        return MODULE4.answer_question()

    return "No games available for your question."

if __name__ == "__main__":
    user_input = input("Please Enter your question: ").lower()
    result = play_game(user_input)
    print(result)
