
from package import *

def main():
    while True:
        question = input('Please enter your question: ').lower()

        if len(question) >= 3:
            module1.run()  # Check MODULE1 first
        elif len(question) >= 3:
            module2.run()  # Then check MODULE2
        # Extend with more modules as needed

if __name__ == "__main__":
    main()
