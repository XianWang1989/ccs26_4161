
print("Hello this program will help you figure out the cost to tile your floor")

while True:
    try:
        x = float(input("Please enter the length of the floor that's being tiled: "))  # Convert to float for calculations
        y = float(input("Next, please enter the width of the floor: "))  # Convert to float for calculations
        fltype = input("Now enter a shape that best describes the room you are getting tiled (circle/ellipse/rectangle/square/triangle): ").lower()

        if fltype in ["circle", "ellipse"]:
            formula = ((x * y) * 0.5) * 3.14
            break
        elif fltype in ["rectangle", "square"]:
            formula = x * y
            break
        elif fltype == "triangle":
            formula = (x * 0.5) * y
            break
        else:
            print("Sorry unrecognized floor type, please try again.")
    except ValueError:
        print("Invalid input, please enter numeric values for length and width.")

while True:
    try:
        tuc = float(input("What is the cost per unit of the tile you'd like: "))  # Convert to float
        pobs = int(input("Please Enter 1 if you are tiling the floor by yourself, otherwise enter 2 for professional flooring: "))

        if pobs == 1:
            total = tuc * formula
            break
        elif pobs == 2:
            labor = float(input("What is the contractor's hourly labor cost? "))  # Convert to float
            total = (tuc * formula) + ((formula / 20) * labor)
            break
        else:
            print("Invalid command, please try again.")
    except ValueError:
        print("Invalid input, please enter numeric values.")

print("The total cost of the tiling project is $" + str(total))
print("Thank you for using my program! Any feedback is appreciated!")
