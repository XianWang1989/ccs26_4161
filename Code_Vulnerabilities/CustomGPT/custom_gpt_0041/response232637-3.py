
from package import *

def main():
    name = input('Please Enter your question: ').lower().split()

    if MODULE1.check_color(name):
        print('You found a color! What is your favorite color?')
        # Add additional color handling here
    elif MODULE2.check_food(name):
        print('You found a food! What is your favorite food?')
        # Add additional food handling here
    else:
        print('No matches found.')

if __name__ == "__main__":
    main()
