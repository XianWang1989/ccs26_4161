
print("Hello, this program will help you figure out the cost to tile your floor")

while True:
    x = input("Please enter the length of the floor that's being tiled: ")
    y = input("Next, please enter the width of the floor: ")

    fltype = input("Now enter a shape that best describes the room you are getting tiled: ").lower()

    if fltype == "circle" or fltype == "ellipse":
        formula = ((float(x) * float(y)) * 0.5) * 3.14
        break

    elif fltype == "rectangle" or fltype == "square":
        formula = float(x) * float(y)
        break

    elif fltype == "triangle":
        formula = (float(x) * 0.5) * float(y)
        break

    else:
        print("Sorry, unrecognized floor type. Please try again.")

while True:
    tuc = input("What is the cost per unit of the tile you'd like: ")

    pobs = input("Please Enter 1 if you are tiling the floor by yourself, otherwise enter 2 for professional flooring: ")

    if pobs == '1':
        total = float(tuc) * formula
        break

    elif pobs == '2':
        labor = input("What is the contractor's hourly labor cost: ")
        total = (float(tuc) * formula) + ((formula / 20) * float(labor))
        break

    else:
        print("Invalid command, please try again.")

print("The total cost of the tiling project is $" + str(total))
print("Thank you for using my program; any feedback is appreciated!")
