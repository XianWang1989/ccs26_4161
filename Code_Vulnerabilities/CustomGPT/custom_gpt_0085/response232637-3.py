
from package import *

def main():
    name = input("Please enter your question: ").lower()

    # Check MODULE1
    response = MODULE1.handle_input(name)
    if response:
        print(response)
        return

    # Check MODULE2
    response = MODULE2.handle_input(name)
    if response:
        print(response)
        return

    # Check more modules as needed
    print("No matching module found for your input.")

if __name__ == "__main__":
    main()
