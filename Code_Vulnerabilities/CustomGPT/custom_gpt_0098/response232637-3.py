
# main.py
from package import *

def main():
    name = input('Please Enter your question: ').lower()
    name2 = name.split()

    # Check each module in sequence
    for module in [MODULE1, MODULE2]:  # Add more modules as needed
        module.run_module(name2)

if __name__ == "__main__":
    main()
