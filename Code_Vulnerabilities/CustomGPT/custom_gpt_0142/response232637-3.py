
# main.py
from package import *

def main():
    name = input('Please Enter your question: ').lower()

    # Check MODULE1 first
    MODULE1.check_color_response(name)

    # Then check MODULE2 if MODULE1 did not process the input
    MODULE2.check_car_response(name)

    # Add more modules as needed with their respective functions.

if __name__ == "__main__":
    main()
