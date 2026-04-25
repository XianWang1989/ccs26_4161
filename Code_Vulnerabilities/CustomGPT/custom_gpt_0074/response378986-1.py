
print("Hello! This program will help you figure out the cost to tile your floor")

while True:  # Loop until a valid floor type is recognized
    x = float(input("Please enter the length of the floor that's being tiled: "))
    y = float(input("Next, please enter the width of the floor: "))

    fltype = input("Now enter a shape that best describes the room you are getting tiled: ").lower()

    if fltype == "circle" or fltype == "ellipse":
        formula = ((x * y) * .5) * 3.14
        break  # Break the loop if a valid shape is recognized
    elif fltype == "rectangle" or fltype == "square":
        formula = x * y
        break
    elif fltype == "triangle":
        formula = (x * .5) * y
        break
    else:
        print("Sorry, unrecognized floor type. Please try again.")

tuc = float(input("What is the cost per unit of the tile you'd like: "))

while True:  # Loop until a valid option for pobs is entered
    pobs = int(input("Please Enter 1 if you are tiling the floor by yourself, otherwise enter 2 for professional flooring: "))

    if pobs == 1:
        total = tuc * formula
        break
    elif pobs == 2:
        labor = float(input("What is the contractor's hourly labor cost? "))
        total = (tuc * formula) + ((formula / 20) * labor)
        break
    else:
        print("Invalid command. Please try again.")

print("The total cost of the tiling project is $" + str(total))
print("Thank you for using my program! Any feedback is appreciated!")
