
# main.py
from package import MODULE1, MODULE2

def main():
    name = input('Please Enter your question: ').lower()
    name2 = name.split()  # Split the input into words

    # Check each module's game
    MODULE1.process_color_game(name2)  # Call function from MODULE1
    MODULE2.process_car_game(name2)     # Call function from MODULE2

if __name__ == "__main__":
    main()
