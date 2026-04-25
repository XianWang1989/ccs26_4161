
from package import *

def main():
    name = input('Please enter your question: ').lower()

    if MODULE1.check_color_question(name):
        name3 = input('What is your favorite color? ')
        print(MODULE1.respond_to_color(name3))
    elif MODULE2.check_car_question(name):
        name3 = input('What is your favorite car? ')
        print(MODULE2.respond_to_car(name3))
    else:
        print("No matching game found.")

if __name__ == "__main__":
    main()
