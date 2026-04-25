
# main.py
from package import *

def main():
    question = input('Please Enter your question: ').lower()

    # Try each module in order until one responds
    for module in [MODULE1, MODULE2, MODULE3]:
        module.main(question)

if __name__ == "__main__":
    main()
