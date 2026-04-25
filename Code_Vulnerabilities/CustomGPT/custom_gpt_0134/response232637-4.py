
# main.py
from package import *

modules = [MODULE1, MODULE2, MODULE3]

def main():
    question = input("Please enter your question: ").lower()
    for module in modules:
        module.run(question)  # Call the module's function

if __name__ == "__main__":
    main()
