
from package import *

def main():
    name = input('Please enter your question: ').lower()

    # Attempt to call the functions in order
    if len(name) >= 3:
        MODULE1.handle_color_question(name)
        MODULE2.handle_car_question(name)
        # Add more modules as needed

if __name__ == "__main__":
    main()
