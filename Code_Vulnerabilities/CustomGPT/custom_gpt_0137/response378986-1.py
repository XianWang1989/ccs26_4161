
print("Hello this program will help you figure out the cost to tile your floor")

while True:
    x = float(input("Please enter the length of the floor that's being tiled: "))
    y = float(input("Next, please enter the width of the floor: "))

    fltype = input("Now enter a shape that best describes the room you are getting tiled: ")
    fltype = fltype.lower()

    # Loop until a valid floor type is entered.
    if fltype == "circle" or fltype == "ellipse":
        formula = ((x * y) * 0.5) * 3.14
        break  # Exit the loop as we have a valid shape

    elif fltype == "rectangle" or fltype == "square":
        formula = x * y
        break  # Exit the loop as we have a valid shape

    elif fltype == "triangle":
        formula = (x * 0.5) * y
        break  # Exit the loop as we have a valid shape

    else:
        print("Sorry unrecognized floor type. Please try again.")

# Loop for the cost per unit of the tile
while True:
    tuc = float(input("What is the cost per unit of the tile you'd like: "))

    pobs = int(input("Please Enter 1 if you are tiling the floor by yourself, otherwise enter 2 for professional flooring: "))

    if pobs == 1:
        total = tuc * formula
        break  # Exit the loop as we have a valid input

    elif pobs == 2:
        labor = float(input("What is the contractor's hourly labor cost: "))
        total = (tuc * formula) + ((formula / 20) * labor)
        break  # Exit the loop as we have a valid input

    else:
        print("Invalid command. Please try again.")

print("The total cost of the tiling project is $" + str(total))
print("Thank you for using my program. Any feedback is appreciated!")
