
import package

def main():
    question = input('Please enter your question: ').lower()

    # Check each module
    for handler in [package.handle_question1, package.handle_question2]:
        response = handler(question)
        if response:
            print(response)
            break
    else:
        print("No relevant module found.")

if __name__ == "__main__":
    main()
