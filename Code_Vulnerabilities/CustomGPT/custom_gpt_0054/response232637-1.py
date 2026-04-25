
from package import *

def main():
    question = input('Please Enter your question: ').lower()

    # Could also use a loop to check against each module's functionality
    if MODULE1.check_answer(question):  # Assuming MODULE1 has a function to check answers
        MODULE1.respond()  # Call the response function of MODULE1
    elif MODULE2.check_answer(question):
        MODULE2.respond()  # Call the response function of MODULE2
    elif MODULE3.check_answer(question):
        MODULE3.respond()  # Call the response function of MODULE3
    # Add more modules as needed
    else:
        print("Sorry, I don't understand your question.")

if __name__ == "__main__":
    main()
