
from package import *

def process_input(user_input):
    name2 = user_input.split()  # Split input into words

    # Check each module's criteria
    if MODULE1.process(name2):
        return
    if MODULE2.process(name2):
        return
    if MODULE3.process(name2):
        return
    if MODULE4.process(name2):
        return

# Main loop
if __name__ == "__main__":
    question = input('Please Enter your question: ').lower()
    process_input(question)
