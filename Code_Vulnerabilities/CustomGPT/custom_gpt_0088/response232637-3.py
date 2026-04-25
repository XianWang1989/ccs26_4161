
from package import MODULE1, MODULE2

def main():
    question = input('Please Enter your question: ').lower()

    for module in [MODULE1, MODULE2]:
        response = module.handle_question(question)
        if response:
            print(response)
            break  # Stop after the first match

if __name__ == "__main__":
    main()
