
# Assuming elemen_data is a dictionary with element names as keys and weights as values
elemen_data = {
    'hydrogen': 1.008,
    'helium': 4.002602,
    'lithium': 6.94,
    # Add more elements as needed
}

choice = int(raw_input("Enter choice (1): "))

if choice == 1:
    noelemen = int(raw_input("Enter total amount of elements: "))
    elements = []

    # Collect the elements in a loop
    for i in range(noelemen):
        element = raw_input(f"Enter element {i + 1}: ")
        elements.append(element)

    # Calculate total weight
    total_weight = 0.0
    for elem in elements:
        weight = float(elemen_data.get(elem.lower(), 0))  # Default to 0 if not found
        total_weight += weight

    print("Total mass =", total_weight)
