
# Sample element data for demonstration
elemen_data = {
    'hydrogen': 1.008,
    'helium': 4.0026,
    'lithium': 6.94,
    # Add more elements as needed
}

# User choice input
choice = int(raw_input("Enter your choice (1 or 2): "))

if choice == 1:
    noelemen = int(raw_input("Enter total amount of elements: "))

    elements = []  # Initialize a list to hold the elements
    total_weight = 0  # Initialize total weight

    # Loop to gather element names
    for i in range(noelemen):
        element = raw_input("Enter element {}: ".format(i + 1))
        elements.append(element.lower())  # Store in list

    # Calculate total weight
    for el in elements:
        weight = elemen_data.get(el)
        if weight is not None:
            total_weight += weight

    print("Total mass =", total_weight)
else:
    print("Invalid choice.")
