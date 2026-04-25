
# Sample elemental data dictionary for demonstration
elemen_data = {
    'hydrogen': 1.008,
    'helium': 4.0026,
    'lithium': 6.94,
    # Add more elements as needed
}

if choice == 1:
    noelemen = int(raw_input("Enter total amount of elements: "))

    elements = []  # Create an empty list to store the user's elements
    total_weight = 0.0  # Variable to accumulate total weight

    # Loop to get user input for the specified number of elements
    for i in range(noelemen):
        element = raw_input("Enter element #{}: ".format(i + 1))
        elements.append(element.lower())  # Store the input in the list

    # Calculate total weight based on user input
    for element in elements:
        weight = float(elemen_data.get(element))  # Get the weight of the element
        if weight is not None:
            total_weight += weight  # Accumulate total weight
        else:
            print("Element '{}' not found in data.".format(element))

    print("Total mass =", total_weight)
