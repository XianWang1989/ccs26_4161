
# Sample element data dictionary for lookup
elemen_data = {
    "hydrogen": 1.00784,
    "helium": 4.002602,
    "lithium": 6.941,
    # Add more elements as needed
}

if choice == 1:
    noelemen = int(input("Enter total amount of elements: "))
    total_weight = 0

    for i in range(noelemen):
        element = input(f"Enter element {i + 1}: ")

        # Look for the weight of the entered element
        weight = elemen_data.get(element.lower())

        if weight is not None:
            total_weight += weight
        else:
            print(f"Element '{element}' not found.")

    print("Total mass =", total_weight)
