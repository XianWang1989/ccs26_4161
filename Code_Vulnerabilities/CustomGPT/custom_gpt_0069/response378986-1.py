
print("Hello, this program will help you figure out the cost to tile your floor")

def get_floor_dimensions():
    x = float(input("Please enter the length of the floor that's being tiled: "))
    y = float(input("Next, please enter the width of the floor: "))
    return x, y

def get_floor_type():
    while True:
        fltype = input("Now enter a shape that best describes the room you are getting tiled: ").lower()
        if fltype in ["circle", "ellipse", "rectangle", "square", "triangle"]:
            return fltype
        else:
            print("Sorry, unrecognized floor type. Please try again.")

def calculate_area(fltype, x, y):
    if fltype in ["circle", "ellipse"]:
        return (x * y * 0.5) * 3.14
    elif fltype in ["rectangle", "square"]:
        return x * y
    elif fltype == "triangle":
        return (x * 0.5) * y

def get_cost_per_unit():
    return float(input("What is the cost per unit of the tile you'd like: "))

def get_flooring_option():
    while True:
        pobs = input("Please enter 1 if you are tiling the floor by yourself, otherwise enter 2 for professional flooring: ")
        if pobs in ['1', '2']:
            return int(pobs)
        else:
            print("Invalid command. Please try again.")

def calculate_total_cost(formula, tuc, pobs):
    if pobs == 1:
        return tuc * formula
    elif pobs == 2:
        labor = float(input("What is the contractor's hourly labor cost? "))
        return (tuc * formula) + ((formula / 20) * labor)

while True:
    x, y = get_floor_dimensions()
    fltype = get_floor_type()
    formula = calculate_area(fltype, x, y)
    tuc = get_cost_per_unit()
    pobs = get_flooring_option()

    total = calculate_total_cost(formula, tuc, pobs)

    print("The total cost of the tiling project is $" + str(total))
    print("Thank you for using my program! Any feedback is appreciated!")

    # Ask if the user wants to run the program again
    cont = input("Would you like to calculate again? (yes/no): ").lower()
    if cont != 'yes':
        break
