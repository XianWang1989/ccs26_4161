
# main.py
from package import *

def main():
    name = input('Please enter your question: ').lower()

    if len(name) >= 3:
        if MODULE1.handle_question(name):
            return
        if MODULE2.handle_question(name):
            return
        if MODULE3.handle_question(name):
            return
    print("No matching module found.")

if __name__ == "__main__":
    main()
