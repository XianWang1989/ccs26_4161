
print("Hello this program will help you figure out the cost to tile your floor")

# Loop for floor type until valid input is received
valid_fltype = False
while not valid_fltype:
    x = float(input("Please enter the length of the floor that's being tiled: "))
    y = float(input("Next, please enter the width of the floor: "))
    fltype = input("Now enter a shape that best describes the room you are getting tiled: ").lower()

    if fltype in ["circle", "ellipse"]:
        formula = ((x * y) * 0.5) * 3.14  # Area for circle-like shapes
        valid_fltype = True

    elif fltype in ["rectangle", "square"]:
        formula = x * y  # Area of rectangle
        valid_fltype = True

    elif fltype == "triangle":
        formula = (x * 0.5) * y  # Area of triangle
        valid_fltype = True

    else:
        print("Sorry unrecognized floor type please contact admin to add shape or try again.")

# Loop for service provider selection until valid input is received
valid_pobs = False
while not valid_pobs:
    tuc = float(input("What is the cost per unit of the tile you'd like: "))
    pobs = int(input("Please Enter 1 if you are tiling the floor by yourself, otherwise enter 2 for professional flooring: "))

    if pobs == 1:
        total = tuc * formula
        valid_pobs = True

    elif pobs == 2:
        labor = float(input("What is the contractor's hourly labor cost? "))
        total = (tuc * formula) + ((formula / 20) * labor)  # Calculate total including labor
        valid_pobs = True

    else:
        print("Invalid command please try again.")

print("The total cost of the tiling project is $" + str(total))
print("Thank you for using my program; any feedback is appreciated!")
