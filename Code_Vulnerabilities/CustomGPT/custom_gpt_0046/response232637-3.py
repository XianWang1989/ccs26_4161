
# main.py
from package import MODULE1, MODULE2  # Import necessary modules

def ask_question():
    question = input('Please enter your question: ').lower()

    # Check MODULE1
    if MODULE1.run(question):
        return

    # Check MODULE2
    if MODULE2.run(question):
        return

    # Add more modules as needed
    print('No relevant module found for your question.')

if __name__ == "__main__":
    ask_question()
