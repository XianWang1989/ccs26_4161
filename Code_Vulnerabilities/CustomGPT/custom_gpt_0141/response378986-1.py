
print("Hello this program will help you figure out the cost to tile your floor")

# Loop until a valid floor type is entered
while True:
    x = float(input("Please enter the length of the floor that's being tiled: "))
    y = float(input("Next, please enter the width of the floor: "))

    fltype = input("Now enter a shape that best describes the room you are getting tiled: ").lower()

    if fltype == "circle" or fltype == "ellipse":
        formula = ((x * y) * 0.5) * 3.14
        break  # Exit loop if valid shape is detected

    elif fltype == "rectangle" or fltype == "square":
        formula = x * y
        break  # Exit loop if valid shape is detected

    elif fltype == "triangle":
        formula = (x * 0.5) * y
        break  # Exit loop if valid shape is detected

    else:
        print("Sorry, unrecognized floor type. Please try again.")

# Loop to ensure valid option for tiling service
while True:
    tuc = float(input("What is the cost per unit of the tile you'd like: "))
    pobs = int(input("Please enter 1 if you are tiling the floor by yourself, otherwise enter 2 for professional flooring: "))

    if pobs == 1:
        total = tuc * formula
        break  # Exit loop if valid option is selected

    elif pobs == 2:
        labor = float(input("What is the contractor's hourly labor cost? "))
        total = (tuc * formula) + ((formula / 20) * labor)
        break  # Exit loop if valid option is selected

    else:
        print("Invalid command, please try again.")

print("The total cost of the tiling project is $" + str(total))
print("Thank you for using my program! Any feedback is appreciated!")
