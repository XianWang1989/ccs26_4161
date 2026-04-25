
elemen_data = {
    'hydrogen': 1.00784,
    'helium': 4.002602,
    'lithium': 6.941,
    # Add more elements as needed
}

# Ask for the number of elements
noelemen = int(raw_input("Enter total amount of elements: "))
total_weight = 0

# Loop through the range based on user input
for i in range(noelemen):
    element = raw_input(f"Enter element {i + 1}: ")

    # Get the weight of the entered element
    weight = float(elemen_data.get(element.lower(), 0))

    if weight > 0:
        total_weight += weight
    else:
        print(f"Element '{element}' not found!")

print("Total mass =", total_weight)
