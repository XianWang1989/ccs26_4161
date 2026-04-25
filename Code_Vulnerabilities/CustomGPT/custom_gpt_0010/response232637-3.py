
from package import *

def main():
    question = input('Please enter your question: ').lower()
    modules = [MODULE1, MODULE2]  # Add MODULE3, MODULE4 as needed

    for module in modules:
        if module.run_module():
            break  # Exit if a module handled the question

if __name__ == "__main__":
    main()
