
# Assume elemen_data is a predefined dictionary with element weights
elemen_data = {
    'hydrogen': 1.01,
    'oxygen': 16.00,
    # Add more elements as needed
}

choice = int(raw_input("Enter 1 to input elements: "))
if choice == 1:
    noelemen = int(raw_input("Enter total amount of elements: "))
    elements = []  # List to store the elements

    for i in range(noelemen):
        element = raw_input("Enter element {}: ".format(i + 1))
        elements.append(element)

    total_weight = 0.0  # Initialize total weight

    for element in elements:
        weight = elemen_data.get(element.lower())
        if weight is not None:
            total_weight += weight
        else:
            print("{} not found in element data.".format(element))

    print("Total mass =", total_weight)
