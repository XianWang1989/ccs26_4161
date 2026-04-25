
# Sample element data dictionary
elemen_data = {
    "hydrogen": 1.008,
    "helium": 4.0026,
    "lithium": 6.94,
    # Add more elements as needed
}

# Get user choice
choice = int(input("Enter 1 to input elements: "))
if choice == 1:
    noelemen = int(input("Enter total amount of elements: "))

    total_weight = 0.0  # Initialize total weight

    for i in range(noelemen):
        element = input(f"Enter element {i + 1}: ")

        # Look for the weight of the entered element
        weight = elemen_data.get(element.lower())

        if weight is not None:
            total_weight += weight  # Add weight to total
        else:
            print(f"Element '{element}' not found in data.")

    print("Total mass =", total_weight)
