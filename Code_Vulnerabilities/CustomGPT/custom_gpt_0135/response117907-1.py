
# Sample data for element weights
elemen_data = {
    'hydrogen': 1.0,
    'helium': 4.0,
    'lithium': 6.9,
    'beryllium': 9.0
}

# Get number of elements from the user
choice = 1  # Assuming user chose option 1 for demonstration
if choice == 1:
    noelemen = int(raw_input("Enter total amount of elements: "))

    # Initialize an empty list to store elements
    elements = []

    # Loop to get the specified number of inputs
    for i in range(noelemen):
        element = raw_input(f"Enter element {i + 1}: ")
        elements.append(element.lower())  # Store input in the list

    total_weight = 0.0  # Initialize total weight

    # Calculate total weight
    for element in elements:
        weight = float(elemen_data.get(element, 0))  # Use 0 if element not found
        total_weight += weight

    print("Total mass =", total_weight)
