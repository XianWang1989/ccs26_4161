
print("Hello! This program will help you figure out the cost to tile your floor.")

while True:
    # Input for floor dimensions
    x = float(input("Please enter the length of the floor that's being tiled: "))
    y = float(input("Next, please enter the width of the floor: "))

    # Loop for floor type
    while True:
        fltype = input("Now enter a shape that best describes the room you are getting tiled: ").lower()

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
            print("Sorry, unrecognized floor type. Please try again.")

    # Input for tile cost
    tuc = float(input("What is the cost per unit of the tile you'd like: "))

    # Loop for tiling method
    while True:
        pobs = input("Please enter 1 if you are tiling the floor by yourself, otherwise enter 2 for professional flooring: ")

        if pobs == '1':
            total = tuc * formula
            break
        elif pobs == '2':
            labor = float(input("What is the contractor's hourly labor cost? "))
            total = (tuc * formula) + ((formula / 20) * labor)
            break
        else:
            print("Invalid command. Please try again.")

    # Output the total cost
    print("The total cost of the tiling project is $" + str(total))
    print("Thank you for using my program! Any feedback is appreciated!")

    # Ask if user wants to run the calculation again
    repeat = input("Would you like to calculate again? (yes/no): ").lower()
    if repeat != 'yes':
        break
