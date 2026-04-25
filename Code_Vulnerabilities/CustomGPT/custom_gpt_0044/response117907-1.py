
# Example data for element weights
elemen_data = {
    'hydrogen': 1.0,
    'helium': 4.0,
    'lithium': 6.9,
    # Add more elements as needed
}

# Ask for the number of elements
choice = 1  # Assuming choice is set to 1
if choice == 1:
    noelemen = int(raw_input("Enter total amount of elements: "))

    elements = []  # List to store user inputs
    total_weight = 0.0  # Initialize total weight

    # Loop to get the required number of elements
    for i in range(noelemen):
        element = raw_input(f"Enter element {i + 1}: ")
        elements.append(element.lower())  # Store in lowercase for consistency

    # Calculate total weight
    for element in elements:
        weight = elemen_data.get(element)
        if weight is not None:
            total_weight += weight
        else:
            print(f"Weight for '{element}' not found.")

    print("Total mass =", total_weight)
