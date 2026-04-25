
print("Hello this program will help you figure out the cost to tile your floor")

while True:
    x = float(input("Please enter the length of the floor that's being tiled: "))
    y = float(input("Next, please enter the width of the floor: "))

    fltype = input("Now enter a shape that best describes the room you are getting tiled: ").lower()

    if fltype in ["circle", "ellipse"]:
        formula = ((x * y) * 0.5) * 3.14

    elif fltype in ["rectangle", "square"]:
        formula = x * y

    elif fltype == "triangle":
        formula = (x * 0.5) * y

    else:
        print("Sorry, unrecognized floor type. Please try again.")
        continue  # Restart the loop if the floor type is unrecognized

    break  # Exit the loop if the floor type is recognized

while True:
    tuc = float(input("What is the cost per unit of the tile you'd like: "))
    pobs = input("Please Enter 1 if you are tiling the floor by yourself, otherwise enter 2 for professional flooring: ")

    if pobs == '1':
        total = tuc * formula
        break  # Exit the loop for valid input as DIY

    elif pobs == '2':
        labor = float(input("What is the contractor's hourly labor cost: "))
        total = (tuc * formula) + ((formula / 20) * labor)
        break  # Exit the loop for valid input for professional

    else:
        print("Invalid command, please try again.")  # Restart the loop for invalid input

print("The total cost of the tiling project is $" + str(total))
print("Thank you for using my program! Any feedback is appreciated!")
