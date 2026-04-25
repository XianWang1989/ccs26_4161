
# main.py
from package import *

def process_question(question):
    if len(question) >= 3:
        if MODULE1.process(question):
            return
        if MODULE2.process(question):
            return
        if MODULE3.process(question):
            return
        if MODULE4.process(question):
            return
        # Add additional modules as needed

if __name__ == "__main__":
    user_input = input("Please enter your question: ").lower()
    process_question(user_input)
