
from package import MODULE1, MODULE2, MODULE3

def run_game():
    question = input("Please enter your question: ").lower()
    for module in [MODULE1, MODULE2, MODULE3]:
        module.play_game()  # Call the play_game function of each module

if __name__ == "__main__":
    run_game()
