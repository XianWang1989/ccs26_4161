
# main.py
from package import *

def main():
    name = input('Please enter your question: ').lower()

    if len(name) >= 3:
        MODULE1.handle_color_question(name)
    if len(name) >= 3:  # Re-evaluate for MODULE2 logic
        MODULE2.handle_food_question(name)
    # Call MODULE3, MODULE4, etc., as needed.

if __name__ == '__main__':
    main()
