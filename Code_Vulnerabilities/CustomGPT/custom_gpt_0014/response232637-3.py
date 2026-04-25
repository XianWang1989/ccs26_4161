
from package import MODULE1, MODULE2

def main():
    question = input('Please enter your question: ').lower()
    # Check each module's handle_question
    if hasattr(MODULE1, 'handle_question'):
        MODULE1.handle_question(question)
    if hasattr(MODULE2, 'handle_question'):
        MODULE2.handle_question(question)

if __name__ == '__main__':
    main()
