
# Sample data for elements and their weights
elemen_data = {
    'hydrogen': 1.008,
    'helium': 4.0026,
    'lithium': 6.94,
    # Add more elements as needed
}

if choice == 1:
    noelemen = int(raw_input("Enter total amount of elements: "))

    total_weight = 0  # Initialize total weight
    elements = []  # List to store the user inputs

    for i in range(noelemen):
        element = raw_input(f"Enter element {i + 1}: ")
        elements.append(element.lower())

    for element in elements:
        weight = elemen_data.get(element)

        if weight is not None:
            total_weight += weight

    print("Total mass =", total_weight)
