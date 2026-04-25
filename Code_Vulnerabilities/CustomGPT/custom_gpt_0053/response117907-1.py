
# Assume elemen_data is a dictionary with element names as keys and weights as values
elemen_data = {
    'hydrogen': 1.008,
    'helium': 4.0026,
    # Add more elements as required
}

choice = int(raw_input("Enter 1 to input elements: "))

if choice == 1:
    noelemen = int(raw_input("Enter total amount of elements: "))
    total_weight = 0.0
    elements = []  # List to store input elements

    for i in range(noelemen):
        element = raw_input(f"Enter element {i+1}: ")
        elements.append(element.lower())  # Store the element in the list

    # Calculate total weight
    for elem in elements:
        weight = elemen_data.get(elem)

        if weight is not None:
            total_weight += weight
        else:
            print(f"Element '{elem}' not found in data.")

    print "Total mass =", total_weight
