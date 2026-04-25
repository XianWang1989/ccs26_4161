
print("Hello, this program will help you figure out the cost to tile your floor.")

# Loop for floor type input
while True:
    x = float(input("Please enter the length of the floor that's being tiled: "))
    y = float(input("Next, please enter the width of the floor: "))

    fltype = input("Now enter a shape that best describes the room you are getting tiled: ").lower()

    if fltype == "circle" or fltype == "ellipse":
        formula = ((x * y) * 0.5) * 3.14
        break  # Break loop if recognized
    elif fltype == "rectangle" or fltype == "square":
        formula = x * y
        break  # Break loop if recognized
    elif fltype == "triangle":
        formula = (x * 0.5) * y
        break  # Break loop if recognized
    else:
        print("Sorry, unrecognized floor type. Please contact admin to add shape or try again.")

# Loop for cost per unit of tile input and the type of project
while True:
    tuc = float(input("What is the cost per unit of the tile you'd like: "))

    pobs = input("Please Enter 1 if you are tiling the floor by yourself, otherwise enter 2 for professional flooring: ")

    if pobs == '1':  # Note: Using string comparison for input
        total = tuc * formula
        break  # Break loop if recognized
    elif pobs == '2':
        labor = float(input("What is the contractor's hourly labor cost? "))
        total = (tuc * formula) + ((formula / 20) * labor)
        break  # Break loop if recognized
    else:
        print("Invalid command, please try again.")

# Output the total cost
print("The total cost of the tiling project is $" + str(total))
print("Thank you for using my program, any feedback is appreciated!")
