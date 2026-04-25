
from package import MODULE1, MODULE2

def main():
    question = input('Please Enter your question: ').lower()

    response = MODULE1.handle_question(question)
    if response is None:
        response = MODULE2.handle_question(question)

    if response:
        print(response)
    else:
        print("No matching module found.")

if __name__ == "__main__":
    main()
