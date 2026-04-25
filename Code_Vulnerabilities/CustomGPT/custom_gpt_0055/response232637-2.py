
# main.py
from package import *

def main():
    name = input('Please Enter your question: ').lower()

    # Check the length of the question
    if len(name) >= 3:
        MODULE1.handle_color_questions(name)
        # You can add more checks for MODULE2, MODULE3, etc.
        # Add similar function calls for other modules
        # For example:
        # elif name in MODULE2.some_other_list:
        #     MODULE2.handle_some_other_questions(name)
        # elif name in MODULE3.another_list:
        #     MODULE3.handle_another_questions(name)

if __name__ == "__main__":
    main()
