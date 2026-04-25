
from package import *

def main():
    question = input('Please enter your question: ').lower()

    for module in [MODULE1, MODULE2, MODULE3]:
        result = module.check_color(question) or module.check_cars(question)
        if result:
            print(result)
            break
    else:
        print("No matching games found.")

if __name__ == "__main__":
    main()
