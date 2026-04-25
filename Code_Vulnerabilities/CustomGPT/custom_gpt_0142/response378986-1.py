
print("Hello, this program will help you figure out the cost to tile your floor")

while True:
    # Get floor dimensions
    try:
        x = float(input("Please enter the length of the floor that's being tiled: "))
        y = float(input("Next, please enter the width of the floor: "))
    except ValueError:
        print("Please enter numeric values for length and width.")
        continue

    fltype = input("Now enter a shape that best describes the room you are getting tiled: ").lower()

    # Calculate area based on type
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

# Get cost per unit of tile
tuc = float(input("What is the cost per unit of the tile you'd like: "))

# Loop for professional or DIY
while True:
    pobs = input("Please enter '1' if you are tiling the floor by yourself, otherwise enter '2' for professional flooring: ")

    if pobs == '1':
        total = tuc * formula
        break
    elif pobs == '2':
        labor = float(input("What is the contractor's hourly labor cost? "))
        total = (tuc * formula) + ((formula / 20) * labor)
        break
    else:
        print("Invalid option, please enter '1' for DIY or '2' for professional.")

# Print total cost
print("The total cost of the tiling project is $" + str(total))
print("Thank you for using my program! Any feedback is appreciated!")
