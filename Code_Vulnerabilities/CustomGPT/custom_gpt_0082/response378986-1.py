
print("Hello, this program will help you figure out the cost to tile your floor.")

while True:
    # Get dimensions of the floor
    x = float(input("Please enter the length of the floor that's being tiled: "))
    y = float(input("Next, please enter the width of the floor: "))

    # Get the floor type and validate it
    fltype = input("Enter a shape that best describes the room (circle, rectangle, triangle, etc.): ").lower()

    if fltype in ["circle", "ellipse"]:
        formula = (x * y * 0.5) * 3.14

    elif fltype in ["rectangle", "square"]:
        formula = x * y

    elif fltype == "triangle":
        formula = (x * 0.5) * y

    else:
        print("Sorry, unrecognized floor type, please try again.")
        continue  # Restart the loop for floor type

    break  # Exit the loop if the floor type is recognized

# Cost per unit of the tile
tuc = float(input("What is the cost per unit of the tile you'd like? "))

while True:
    pobs = int(input("Please enter 1 if you are tiling the floor by yourself, otherwise enter 2 for professional flooring: "))

    if pobs == 1:
        total = tuc * formula
        break  # Exit the loop for valid input

    elif pobs == 2:
        labor = float(input("What is the contractor's hourly labor cost? "))
        total = (tuc * formula) + ((formula / 20) * labor)
        break  # Exit the loop for valid input

    else:
        print("Invalid command, please try again.")

# Output the total cost
print("The total cost of the tiling project is $" + str(total))
print("Thank you for using my program; any feedback is appreciated!")
