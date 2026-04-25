
# Sample element data for demonstration
elemen_data = {
    'hydrogen': 1.008,
    'helium': 4.0026,
    'lithium': 6.94,
    # Add more elements as needed
}

choice = int(raw_input("Enter your choice (1): "))
if choice == 1:
    noelemen = int(raw_input("Enter total amount of elements: "))

    elements = []  # List to store the element names

    # Collect input for the number of elements specified
    for i in range(noelemen):
        element = raw_input(f"Enter element {i + 1}: ")
        elements.append(element.lower())  # Store elements as lowercase

    total_weight = 0.0  # Initialize total weight

    # Calculate total weight of the entered elements
    for el in elements:
        weight = float(elemen_data.get(el))
        if weight is not None:
            total_weight += weight
        else:
            print(f"Element '{el}' not found in the data.")

    print("Total mass =", total_weight)
