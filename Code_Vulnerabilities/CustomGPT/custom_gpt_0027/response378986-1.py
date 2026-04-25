
print("Hello, this program will help you figure out the cost to tile your floor")

while True:
    x = float(input("Please enter the length of the floor that's being tiled: "))
    y = float(input("Next, please enter the width of the floor: "))

    fltype = input("Now enter a shape that best describes the room you are getting tiled: ").lower()

    if fltype == "circle" or fltype == "ellipse":
        formula = ((x * y) * 0.5) * 3.14

    elif fltype == "rectangle" or fltype == "square":
        formula = x * y

    elif fltype == "triangle":
        formula = (x * 0.5) * y

    else:
        print("Sorry, unrecognized floor type. Please try again.")
        continue  # restart the loop

    while True:
        tuc = float(input("What is the cost per unit of the tile you'd like: "))
        pobs = input("Please enter 1 if you are tiling the floor by yourself, otherwise enter 2 for professional flooring: ")

        if pobs == '1':
            total = tuc * formula
            break  # valid input, exit inner loop

        elif pobs == '2':
            labor = float(input("What is the contractor's hourly labor cost? "))
            total = (tuc * formula) + ((formula / 20) * labor)
            break  # valid input, exit inner loop

        else:
            print("Invalid command, please try again.")

    print("The total cost of the tiling project is $" + str(total))
    print("Thank you for using my program! Any feedback is appreciated!")

    # Optionally ask if the user wants to calculate again
    another = input("Would you like to do another calculation? (yes/no): ").lower()
    if another != 'yes':
        break
