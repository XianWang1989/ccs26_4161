
# Simulated element data for demonstration
elemen_data = {
    'hydrogen': 1.008,
    'helium': 4.0026,
    'lithium': 6.94,
    # Add more elements as needed
}

# Get the number of elements from the user
if choice == 1:
    noelemen = int(raw_input("Enter total amount of elements: "))
    elements = []

    # Loop to collect element names
    for i in range(noelemen):
        element = raw_input(f"Enter element {i + 1}: ")
        elements.append(element.lower())

    # Calculate total weight
    total_weight = 0
    for el in elements:
        weight = float(elemen_data.get(el))
        if weight is not None:
            total_weight += weight

    print "Total mass =", total_weight
