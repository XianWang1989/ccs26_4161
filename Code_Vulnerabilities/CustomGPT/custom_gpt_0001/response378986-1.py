
print("Hello, this program will help you figure out the cost to tile your floor.")

# Loop until valid floor dimensions and type
while True:
    x = input("Please enter the length of the floor that's being tiled: ")
    y = input("Next, please enter the width of the floor: ")

    fltype = input("Now enter a shape that best describes the room you are getting tiled: ")
    fltype = fltype.lower()

    try:
        x = float(x)
        y = float(y)
    except ValueError:
        print("Please enter valid numerical values for length and width.")
        continue

    # Check floor type and calculate area
    if fltype == "circle" or fltype == "ellipse":
        formula = ((x * y) * 0.5) * 3.14
        break
    elif fltype == "rectangle" or fltype == "square":
        formula = x * y
        break
    elif fltype == "triangle":
        formula = (x * 0.5) * y
        break
    else:
        print("Sorry, unrecognized floor type. Please try again.")

# Loop until valid cost per unit input
while True:
    try:
        tuc = float(input("What is the cost per unit of the tile you'd like: "))
        break
    except ValueError:
        print("Please enter a valid numerical value for the cost per unit.")

# Loop until valid option for tiling method is input
while True:
    pobs = input("Please enter 1 if you are tiling the floor by yourself, otherwise enter 2 for professional flooring: ")

    if pobs == "1":
        total = tuc * formula
        break
    elif pobs == "2":
        labor = input("What is the contractor's hourly labor cost: ")
        try:
            labor = float(labor)
            total = (tuc * formula) + ((formula / 20) * labor)
            break
        except ValueError:
            print("Please enter a valid numerical value for the contractor's labor cost.")
    else:
        print("Invalid command, please try again.")

print("The total cost of the tiling project is $" + str(total))
print("Thank you for using my program! Any feedback is appreciated!")
