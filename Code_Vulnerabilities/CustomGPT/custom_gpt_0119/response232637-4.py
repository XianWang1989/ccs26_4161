
from package import *

def main():
    name = input('Please enter your question: ').lower()
    name2 = name.split()  # Splitting input into words

    # Check each module in order
    if not MODULE1.check_color(name2):
        if not MODULE2.check_car(name2):
            MODULE3.check_food(name2)

if __name__ == "__main__":
    main()
