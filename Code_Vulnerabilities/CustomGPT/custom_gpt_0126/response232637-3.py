
# main.py
from package import *

def main():
    name = input('Please enter your question: ').lower().split()

    # Check each module
    if MODULE1.handle_input(name):
        return
    if MODULE2.handle_input(name):
        return
    if MODULE3.handle_input(name):
        return
    if MODULE4.handle_input(name):
        return

if __name__ == "__main__":
    main()
