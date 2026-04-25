
from package import *

def main():
    name = input('Please enter your question: ').lower()
    name2 = name.split()  # Split input into words

    if len(name2) >= 3:
        MODULE1.check_color(name2)
        MODULE2.check_cars(name2)
        MODULE3.check_foods(name2)
        # Add more modules as needed

if __name__ == "__main__":
    main()
