
print("Hello! This program will help you figure out the cost to tile your floor")

# Loop to keep prompting for valid floor dimensions and type
while True:
    x = float(input("Please enter the length of the floor that's being tiled: "))
    y = float(input("Next, please enter the width of the floor: "))

    fltype = input("Now enter a shape that best describes the room you are getting tiled: ").lower()

    if fltype == "circle" or fltype == "ellipse":
        formula = ((x * y) * 0.5) * 3.14
        break  # Valid shape found, exit the loop

    elif fltype == "rectangle" or fltype == "square":
        formula = x * y
        break  # Valid shape found, exit the loop

    elif fltype == "triangle":
        formula = (x * 0.5) * y
        break  # Valid shape found, exit the loop

    else:
        print("Sorry, unrecognized floor type. Please try again.")

# Loop to ensure valid cost per unit input
while True:
    try:
        tuc = float(input("What is the cost per unit of the tile you'd like: "))
        break  # Valid input, exit the loop
    except ValueError:
        print("Invalid input. Please enter a numerical value.")

# Loop to ensure valid pobs input
while True:
    try:
        pobs = int(input("Please enter 1 if you are tiling the floor by yourself, otherwise enter 2 for professional flooring: "))
        if pobs == 1 or pobs == 2:
            break  # Valid input, exit the loop
        else:
            print("Invalid command. Please enter either 1 or 2.")
    except ValueError:
        print("Invalid input. Please enter either 1 or 2.")

# Calculate total cost based on pobs choice
if pobs == 1:
    total = tuc * formula
else:
    labor = float(input("What is the contractor's hourly labor cost? "))
    total = (tuc * formula) + ((formula / 20) * labor)

print("The total cost of the tiling project is $" + str(total))
print("Thank you for using my program! Any feedback is appreciated!")
