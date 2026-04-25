
from package import MODULE1, MODULE2

def main():
    question = input('Please enter your question: ').lower()

    modules = [MODULE1, MODULE2]
    for module in modules:
        if module.handle_query(question):
            break
    else:
        print("No suitable module found for the question.")

if __name__ == "__main__":
    main()
