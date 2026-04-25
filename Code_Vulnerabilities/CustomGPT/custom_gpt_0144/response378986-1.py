print("Hello! This program will help you figure out the cost to tile your floor.")

# Get floor dimensions
x = float(input("Please enter the length of the floor (in feet): "))
y = float(input("Next, please enter the width of the floor (in feet): "))

# Loop until valid floor type is entered
while True:
    fltype = input("Now enter a shape that best describes the room (circle, rectangle, triangle, etc.): ").lower()
    if fltype in ["circle", "ellipse"]:
        formula = ((x * y) * 0.5) * 3.14
        break
    elif fltype in ["rectangle", "square"]:
        formula = x * y
        break
    elif fltype == "triangle":
        formula = (x * y) * 0.5
        break
    else:
        print("Sorry, unrecognized floor type. Please try again.")

# Get tile unit cost
tuc = float(input("What is the cost per unit of the tile you'd like (in dollars): "))

# Loop until valid labor option is chosen
while True:
    pobs = input("Enter 1 if you are tiling the floor yourself, or 2 for professional installation: ")
    if pobs == "1":
        total = tuc * formula
        break
    elif pobs == "2":
        labor = float(input("What is the contractor's hourly labor cost (in dollars): "))
        total = (tuc * formula) + ((formula / 20) * labor)  # assuming 20 sq ft/hr
        break
    else:
        print("Invalid input. Please enter 1 or 2.")

# Show total cost
print("The total cost of the tiling project is $" + str(round(total, 2)))
print("Thank you for using this program! Any feedback is appreciated.")
