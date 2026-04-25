
# Assume elemen_data is a dictionary with element names as keys and weights as values
elemen_data = {
    'hydrogen': 1.008,
    'helium': 4.0026,
    'lithium': 6.94,
    # Add more elements as needed
}

choice = int(raw_input("Enter 1 to input elements: "))

if choice == 1:
    noelemen = int(raw_input("Enter total amount of elements: "))
    elements = []

    # Collect user inputs
    for i in range(noelemen):
        element = raw_input("Enter element {}: ".format(i + 1))
        elements.append(element.lower())

    total_weight = 0.0

    # Calculate total weight
    for element in elements:
        weight = elemen_data.get(element)
        if weight is not None:
            total_weight += weight
        else:
            print("Element '{}' not found in data.".format(element))

    print("Total mass =", total_weight)
