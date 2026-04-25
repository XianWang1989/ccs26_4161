
from package import *

def main():
    name = input('Please Enter your question: ').lower()

    # List of functions to call based on input
    modules = [MODULE1.run, MODULE2.run, MODULE3.run, MODULE4.run]

    for module in modules:
        if name in module.__code__.co_names:
            module()
            break  # Stop if one module runs successfully

if __name__ == "__main__":
    main()
