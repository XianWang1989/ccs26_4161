
# Sample element data
elemen_data = {
    'hydrogen': 1.008,
    'oxygen': 16.00,
    'carbon': 12.01
    # Add more elements as needed
}

choice = int(raw_input("Enter choice (1 for elements): "))
if choice == 1:
    noelemen = int(raw_input("Enter total amount of elements: "))

    total_weight = 0.0
    elements = []  # List to store input elements

    for i in range(noelemen):
        element = raw_input("Enter element {}: ".format(i + 1))
        elements.append(element.lower())  # Add to list and convert to lowercase

    # Calculate total weight
    for el in elements:
        weight = float(elemen_data.get(el))
        if weight is not None:
            total_weight += weight
        else:
            print("Element '{}' not found in data.".format(el))

    print("Total mass =", total_weight)
