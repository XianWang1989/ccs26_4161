
# Import all modules from the package
from package import *

def main():
    question = input('Please enter your question: ').lower()

    # You can define a list of functions or checks from each module
    modules = [MODULE1.process_question,
               MODULE2.process_question,
               MODULE3.process_question,
               MODULE4.process_question]

    # Iterate through each module's process function
    for module in modules:
        if module(question):
            break  # Stop if one module successfully handles the question

if __name__ == "__main__":
    main()
