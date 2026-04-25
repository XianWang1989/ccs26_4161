
# main_program.py
from package import MODULE1, MODULE2  # Import only the specific modules needed

def main():
    question = input('Please Enter your question: ').lower()

    # Check each module to handle the question
    if not MODULE1.handle_question(question):  # Check MODULE1
        if not MODULE2.handle_question(question):  # Check MODULE2
            print("Sorry, I don't understand that question.")

if __name__ == "__main__":
    main()
