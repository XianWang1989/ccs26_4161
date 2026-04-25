
from package import *

def main():
    name = input('Please Enter your question: ').lower()

    # Check in MODULE1
    response = MODULE1.check_color(name)
    if response:
        print(response)
    else:
        # Check in MODULE2 if MODULE1 doesn't provide a response
        response = MODULE2.check_cars(name)
        if response:
            print(response)
        else:
            print("No matches found in any module.")

if __name__ == '__main__':
    main()
