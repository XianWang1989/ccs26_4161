
# Sample element data
elemen_data = {
    'hydrogen': 1.008,
    'helium': 4.0026,
    'lithium': 6.94,
    # Add more elements as needed
}

# Get the number of elements to enter
choice = int(raw_input("Choose an option (1): "))
if choice == 1:
    noelemen = int(raw_input("Enter total amount of elements: "))

    weights = []  # List to store the weights
    total_weight = 0  # Initialize total weight

    # Loop to get the elements
    for i in range(noelemen):
        element = raw_input(f"Enter element {i + 1}: ")
        weight = elemen_data.get(element.lower())

        if weight is not None:
            weights.append(weight)  # Append the weight to the list
            total_weight += weight  # Add to total weight
        else:
            print(f"Element '{element}' not found in database.")

    print("Total mass =", total_weight)
