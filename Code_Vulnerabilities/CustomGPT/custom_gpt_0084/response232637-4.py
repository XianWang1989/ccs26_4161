
from package import *

def main():
    name = input('Please Enter your question: ').lower()

    modules = [MODULE1, MODULE2, MODULE3]  # Add more modules as needed
    for module in modules:
        response = module.run_module(name)
        if response:
            print(response)
            break  # Exit the loop on first successful module

if __name__ == "__main__":
    main()
