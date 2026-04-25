
def main():
    print("Hello! This program will help you figure out the cost to tile your floor")

    while True:
        # Getting dimensions of the floor
        x = float(input("Please enter the length of the floor that's being tiled: "))
        y = float(input("Next, please enter the width of the floor: "))

        # Getting the floor type with validation
        while True:
            fltype = input("Now enter a shape that best describes the room you are getting tiled: ").lower()

            if fltype in ["circle", "ellipse"]:
                formula = (x * y * 0.5) * 3.14  # Area formula for a circle/ellipse
                break
            elif fltype in ["rectangle", "square"]:
                formula = x * y  # Area formula for a rectangle/square
                break
            elif fltype == "triangle":
                formula = (x * 0.5) * y  # Area formula for a triangle
                break
            else:
                print("Sorry, unrecognized floor type. Please try again.")

        # Cost per unit of the tile
        tuc = float(input("What is the cost per unit of the tile you'd like: "))

        # Getting flooring option with validation
        while True:
            pobs = input("Please enter 1 if you are tiling the floor by yourself, otherwise enter 2 for professional flooring: ")

            if pobs == "1":
                total = tuc * formula
                break
            elif pobs == "2":
                labor = float(input("What is the contractor's hourly labor cost: "))
                total = (tuc * formula) + ((formula / 20) * labor)  # Adjust as necessary for labor hours
                break
            else:
                print("Invalid command, please try again.")

        # Output the total cost
        print("The total cost of the tiling project is $" + str(total))
        print("Thank you for using my program! Any feedback is appreciated!")

        # Ask if the user wants to run the program again
        another_round = input("Would you like to calculate again? (yes/no): ").lower()
        if another_round != 'yes':
            break

if __name__ == "__main__":
    main()
