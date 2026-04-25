
from package import *

def main():
    name = input('Please enter your question: ').lower()

    for module in [MODULE1, MODULE2, MODULE3]:
        if module.process_question(name):
            break

if __name__ == "__main__":
    main()
