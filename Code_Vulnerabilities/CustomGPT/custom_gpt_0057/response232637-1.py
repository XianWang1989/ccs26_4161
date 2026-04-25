
# MAIN PROGRAM

from package import *

def run_modules(question):
    modules = [MODULE1, MODULE2, MODULE3, MODULE4]  # List your modules
    for module in modules:
        if module.check_question(question):
            module.run_game()  # Assuming each module has a run_game function
            break
    else:
        print("No game available for this question.")

if __name__ == "__main__":
    question = input('Please Enter your question: ').lower()
    run_modules(question)

# MODULE1.py
def check_question(question):
    colorLists = ['what is my color', 'color']
    return any(item in question for item in colorLists)

def run_game():
    name3 = input('What is your favorite color? ').strip().lower()
    responses = {
        'red': 'You are hot!',
        'pink': 'You must be a lady!',
        'blue': 'Boys love this!'
    }
    print(responses.get(name3, 'Color not recognized!'))

# Repeat similar structure for MODULE2, MODULE3, MODULE4, etc.
