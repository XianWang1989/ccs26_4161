
# Assume elemen_data is a dictionary containing element names and their weights
elemen_data = {
    'hydrogen': 1.008,
    'helium': 4.0026,
    # Add more elements as needed
}

if choice == 1:
    noelemen = int(raw_input("Enter total amount of elements: "))
    total_weight = 0

    # List to hold user input
    elements = []

    # Collect user input
    for i in range(noelemen):
        element = raw_input("Enter element {}: ".format(i + 1))
        elements.append(element)

    # Calculate total weight
    for element in elements:
        weight = elemen_data.get(element.lower())
        if weight is not None:
            total_weight += weight
        else:
            print("Element '{}' not found in data.".format(element))

    print("Total mass =", total_weight)
