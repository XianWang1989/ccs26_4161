
# main.py
from package import *

# Function to handle user input and call the appropriate module function
def handle_input(question):
    if MODULE1.process_question(question):
        return
    if MODULE2.process_question(question):
        return
    if MODULE3.process_question(question):
        return
    # Add other modules as needed

# Main loop
if __name__ == '__main__':
    user_question = input('Please Enter your question: ').lower()
    handle_input(user_question)
