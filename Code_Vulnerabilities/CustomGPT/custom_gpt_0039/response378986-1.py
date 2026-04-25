
print("Hello this program will help you figure out the cost to tile your floor")

while True:
    x = float(input("Please enter the length of the floor that's being tiled: "))
    y = float(input("Next, please enter the width of the floor: "))

    fltype = input("Now enter a shape that best describes the room you are getting tiled: ").lower()

    if fltype in ["circle", "ellipse"]:
        formula = ((x * y) * 0.5) * 3.14

    elif fltype in ["rectangle", "square"]:
        formula = x * y

    elif fltype == "triangle":
        formula = (x * 0.5) * y

    else:
        print("Sorry, unrecognized floor type. Please try again.")
        continue  # Go back to the beginning of the loop

    # Loop for cost per unit
    while True:
        try:
            tuc = float(input("What is the cost per unit of the tile you'd like: "))
            break  # If input is valid, exit the loop
        except ValueError:
            print("Please enter a valid number for the cost.")

    # Loop for project option
    while True:
        pobs = input("Please Enter 1 if you are tiling the floor by yourself, otherwise enter 2 for professional flooring: ")
        if pobs == '1':
            total = tuc * formula
            break  # Exit the loop for valid input
        elif pobs == '2':
            labor = float(input("What is the contractor's hourly labor cost: "))
            total = (tuc * formula) + ((formula / 20) * labor)
            break  # Exit the loop for valid input
        else:
            print("Invalid command, please try again.")

    print("The total cost of the tiling project is $" + str(total))
    print("Thank you for using my program! Any feedback is appreciated!")
    break  # Exit the main loop after calculation
