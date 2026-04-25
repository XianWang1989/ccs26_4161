
print("Hello, this program will help you figure out the cost to tile your floor")

while True:
    # Get room dimensions
    x = float(input("Please enter the length of the floor that's being tiled: "))
    y = float(input("Next, please enter the width of the floor: "))

    fltype = input("Now enter a shape that best describes the room you are getting tiled: ").lower()

    # Calculate based on floor type
    if fltype in ("circle", "ellipse"):
        formula = ((x * y) * 0.5) * 3.14  # Area of an ellipse
        break  # Exit loop if recognized

    elif fltype in ("rectangle", "square"):
        formula = x * y  # Area of a rectangle or square
        break  # Exit loop if recognized

    elif fltype == "triangle":
        formula = (x * 0.5) * y  # Area of a triangle
        break  # Exit loop if recognized

    else:
        print("Sorry, unrecognized floor type. Please try again.")

# Loop for tile cost input
while True:
    try:
        tuc = float(input("What is the cost per unit of the tile you'd like: "))
        break  # Exit loop if valid input
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

# Loop for professional vs. DIY tiling
while True:
    pobs = input("Please Enter 1 if you are tiling the floor by yourself, otherwise enter 2 for professional flooring: ")

    if pobs == "1":
        total = tuc * formula
        break  # Exit loop if recognized

    elif pobs == "2":
        labor = float(input("What is the contractor's hourly labor cost: "))
        total = (tuc * formula) + ((formula / 20) * labor)
        break  # Exit loop if recognized

    else:
        print("Invalid command. Please try again.")

# Output the total cost
print("The total cost of the tiling project is $" + str(total))
print("Thank you for using my program! Any feedback is appreciated!")
