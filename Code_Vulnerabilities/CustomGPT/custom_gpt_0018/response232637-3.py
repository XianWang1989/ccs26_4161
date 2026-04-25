
from package import *

def main():
    name = input('Please Enter your question: ').lower()

    # Check in MODULE1
    if len(name) >= 3:
        MODULE1.check_color(name)

    # Check in MODULE2 if MODULE1 does not handle it
    elif len(name) >= 3:
        MODULE2.check_cars(name)

    # Add more checks for MODULE3, MODULE4, etc., as necessary...

if __name__ == "__main__":
    main()
