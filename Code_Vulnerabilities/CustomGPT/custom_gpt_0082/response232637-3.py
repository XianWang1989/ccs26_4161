
# main.py
from package import *

def main():
    name = input('Please enter your question: ').lower()

    # Check MODULE1
    if MODULE1.check_for_color(name):
        return  # Exit after MODULE1

    # Check MODULE2
    if MODULE2.check_for_toy(name):
        return  # Exit after MODULE2

    print('No matches found in any modules.')

if __name__ == '__main__':
    main()
