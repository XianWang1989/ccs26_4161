
from package import *

def main():
    question = input('Please Enter your question: ').lower()
    if 'color' in question:
        MODULE1.run_game()
    elif 'car' in question:
        MODULE2.run_game()
    # Add more conditions for MODULE3, MODULE4, etc.

if __name__ == '__main__':
    main()
