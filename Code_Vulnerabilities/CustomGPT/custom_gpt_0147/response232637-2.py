
from package.MODULE1 import run_game as run_game_1
from package.MODULE2 import run_game as run_game_2
from package.MODULE3 import run_game as run_game_3

def main():
    while True:
        user_question = input('Please Enter your question: ').lower()

        # Check each module in order
        if run_game_1(user_question):
            break  # If game handled the question, exit loop
        elif run_game_2(user_question):
            break
        elif run_game_3(user_question):
            break
        else:
            print("Sorry, I don't understand your question.")
            continue  # Ask for input again

if __name__ == '__main__':
    main()
