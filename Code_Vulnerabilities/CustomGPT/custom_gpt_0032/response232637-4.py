
from package import *

def main():
    question = input('Please enter your question: ').lower()

    # Check each module
    response = MODULE1.check_color(question)
    if response:
        print(response)
    else:
        response = MODULE2.check_food(question)
        if response:
            print(response)
        else:
            response = MODULE3.check_toy(question)
            if response:
                print(response)
            else:
                print("No matches found.")

if __name__ == '__main__':
    main()
