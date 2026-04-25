
# Define a dictionary with some example element weights
elemen_data = {
    'hydrogen': 1.00784,
    'helium': 4.002602,
    'lithium': 6.941,
    # Add other elements as needed
}

# Indicate the choice for processing
choice = int(raw_input("Enter your choice (1 to input elements): "))

if choice == 1:
    noelemen = int(raw_input("Enter total amount of elements: "))
    elements = []  # List to store element names

    for i in range(noelemen):
        element = raw_input("Enter element {}: ".format(i + 1))
        elements.append(element.lower())  # Collect and store the element in the list

    total_weight = 0  # Initialize total weight
    for element in elements:
        weight = elemen_data.get(element)
        if weight is not None:
            total_weight += weight  # Accumulate weight
        else:
            print("Element '{}' not found in the data.".format(element))

    print("Total mass =", total_weight)
